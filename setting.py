import PySimpleGUI as sg
import configparser

def is_true(value):
    return False if value == 'False' else bool(value)

def open_setting():
    ini = configparser.ConfigParser()
    ini.read('.\setting.ini','UTF-8')
    fukou_setting: bool = is_true(ini.get('setting','fukou'))
    weather_setting: bool = is_true(ini.get('setting','weather'))
    region_setting: int = ini.get('setting','region')
    values_region = ['北海道','東北','関東','中部','近畿','中国','四国','九州']
    layout = [[sg.Text("表示設定", key="new")],[sg.Checkbox('天気予報', default=weather_setting)],[sg.Text('地域', size=(4, 1)),sg.Combo(values_region, default_value=values_region[int(region_setting)], size=(20,1)) ],[sg.Checkbox('不幸ガチャ', default=fukou_setting)],[sg.Button("Apply")]]
    window = sg.Window("Settings", layout, modal=True)
    choice = None
    while True:
        event, values = window.read()
        if event == "Apply":
            ini2 = configparser.ConfigParser()
            ini2['setting'] = {}
            ini2['setting']['weather'] = str(values[0])
            ini2['setting']['region'] = str(values_region.index(str(values[1])))
            ini2['setting']['fukou'] = str(values[2])
            
            with open('./setting.ini','w') as configfile:
                ini2.write(configfile)
            break
        elif event == sg.WINDOW_CLOSED: 
            break
    window.close()

def get_show_list():
    values_region = ['北海道','東北','関東','中部','近畿','中国','四国','九州']
    ini = configparser.ConfigParser()
    ini.read('.\setting.ini','UTF-8')
    fukou_setting: bool = is_true(ini.get('setting','fukou'))
    weather_setting: bool = is_true(ini.get('setting','weather'))
    region_setting: str = values_region[int(ini.get('setting','region'))]
    return [fukou_setting,region_setting,weather_setting]
  
#open_setting()
