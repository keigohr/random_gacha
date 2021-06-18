import PySimpleGUI as sg
import base64
import setting
import weather_prediction
import weather_random
import mamechishiki
import webbrowser
import insi_gacha
import sosuu_gacha


def image_file_to_base64(file_path):
    with open(file_path, "rb") as image_file:
        data = base64.b64encode(image_file.read())

    return data.decode('utf-8')


button_weather = image_file_to_base64('./button_image/button_weather.png')
button_inshi = image_file_to_base64('./button_image/button_inshi.png')
button_prime = image_file_to_base64('./button_image/button_prime.png')
button_custom = image_file_to_base64('./button_image/button_custom.png')
button_setting = image_file_to_base64('./button_image/setting.png')
button_add = image_file_to_base64('./button_image/add.png')
button_tweet = image_file_to_base64('./button_image/button_tweet.png')
logo = image_file_to_base64('./img/logo.png')

sg.change_look_and_feel('LightBrown3')

background = sg.LOOK_AND_FEEL_TABLE['LightBrown3']['BACKGROUND']

layout = [  [sg.Image(filename='./img/logo.png')],
            [
                sg.Button(key='weather', image_data=button_weather,border_width=0,use_ttk_buttons=True, button_color=('LightYellow3',background)),
                sg.Button(key='inshi', image_data=button_inshi, border_width=0,use_ttk_buttons=True, button_color=('LightYellow3',background)),
            ],
            [
                sg.Button(key='prime', image_data=button_prime, border_width=0,use_ttk_buttons=True, button_color=('LightYellow3',background)),
                sg.Button(key='custom1', image_data=button_custom, border_width=0,use_ttk_buttons=True, button_color=('LightYellow3',background)),
            ],
            [
                sg.Button(key='setting', image_data=button_setting, border_width=0,use_ttk_buttons=True, button_color=('LightYellow3',background)),
                sg.Button(key='add', image_data=button_add, border_width=0,use_ttk_buttons=True, button_color=('LightYellow3',background)),
            ],
            [sg.HorizontalSeparator()],
            mamechishiki.get_mamechishiki_list()
        ]


window = sg.Window('Nandemo Gacha', layout, use_default_focus=False, element_justification='c')


def open_window(func, title):
    tweet, theme, _layout = func()
    _layout.append([sg.Button(key="tweet", border_width=0, image_data=button_tweet, button_color=('SkyBlue3','#1DA0F1'))])
    sg.theme(theme)
    _url = 'https://twitter.com/intent/tweet?text='
    _url += tweet
    _window = sg.Window(title, _layout, modal=True, use_default_focus=False, element_justification='c')
    choice = None
    while True:
        _event, _values = _window.read()
        if _event == "Exit" or _event == sg.WIN_CLOSED:
            break
        if _event == "tweet":
            webbrowser.open(_url)
    sg.theme('LightBrown3')
    _window.close()


while True:
    event, values = window.read()
    if event.startswith("URL "):
        url = event.split(' ')[1]
        webbrowser.open(url)
    #  xボタンが押されたら閉じる
    if event == sg.WINDOW_CLOSED:
        break
    #  メニューバーの「設定」が押されたら設定画面を開く
    if event == 'setting':
        setting.open_setting()
    if event == 'add':
        setting.open_addition()
    if event == 'weather':
        open_window(weather_random.return_weather, "Weather Gacha")
    if event == 'inshi':
        open_window(insi_gacha.insi_gacha, "Inshi Gacha")
    if event == 'prime':
        open_window(sosuu_gacha.sosuu_gacha, "Prime Gacha")
    if event == 'custom1':
        add = str(setting.get_show_list()[4])
        name1, name2, name3 = setting.addition_name()

        if add == name1:
            open_window(setting.get_addition_result, name1, 1)
        if add == name2:
            open_window(setting.get_addition_result, name2, 2)
        if add == name3:
            open_window(setting.get_addition_result, name3, 3)

window.close()
