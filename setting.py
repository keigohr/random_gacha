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
    trivia_setting: bool = is_true(ini.get('setting','trivia'))
    addition1_setting: bool = is_true(ini.get('setting','addition1'))
    addition2_setting: bool = is_true(ini.get('setting','addition2'))
    addition3_setting: bool = is_true(ini.get('setting','addition3'))
    values_region = ['北海道','東北','関東','中部','近畿','中国','四国','九州']
    ini1 = configparser.ConfigParser()
    ini1.read('./addition1.ini','UTF-8')
    name1_setting:str = ini1.get('setting','name')
    ini2 = configparser.ConfigParser()
    ini2.read('./addition2.ini','UTF-8')
    name2_setting:str = ini2.get('setting','name')
    ini3 = configparser.ConfigParser()
    ini3.read('./addition3.ini','UTF-8')
    name3_setting:str = ini3.get('setting','name')
    layout = [[sg.Text("表示設定", key="new")],[sg.Checkbox('天気予報', default=weather_setting)],[sg.Text('地域', size=(4, 1)),sg.Combo(values_region, default_value=values_region[int(region_setting)], size=(20,1)) ],[sg.Checkbox('不幸ガチャ', default=fukou_setting)],[sg.Checkbox('豆知識', default=trivia_setting)],[sg.Checkbox('追加ガチャ1: '+name1_setting, default=addition1_setting)],[sg.Checkbox('追加ガチャ2: '+name2_setting, default=addition2_setting)],[sg.Checkbox('追加ガチャ3: '+name3_setting, default=addition3_setting)],[sg.Button("Apply")]]
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
            ini2['setting']['trivia'] = str(values[3])
            ini2['setting']['addition1'] = str(values[4])
            ini2['setting']['addition2'] = str(values[5])
            ini2['setting']['addition3'] = str(values[6])
            
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
    trivia_setting: bool = is_true(ini.get('setting','trivia'))
    addition1_settiong: bool = is_true(ini.get('setting','addition1'))
    addition2_settiong: bool = is_true(ini.get('setting','addition2'))
    addition3_settiong: bool = is_true(ini.get('setting','addition3'))
    return [fukou_setting,region_setting,weather_setting,trivia_setting,addition1_settiong,addition2_settiong,addition3_settiong]

def open_addition():
    ini1 = configparser.ConfigParser()
    ini1.read('./addition1.ini','UTF-8')
    name1_setting:str = ini1.get('setting','name')
    ini2 = configparser.ConfigParser()
    ini2.read('./addition2.ini','UTF-8')
    name2_setting:str = ini2.get('setting','name')
    ini3 = configparser.ConfigParser()
    ini3.read('./addition3.ini','UTF-8')
    name3_setting:str = ini3.get('setting','name')
    layout = [[sg.Text("追加選択", key="new")],[sg.Button("追加ガチャ1"),sg.Text('ガチャ名: '+name1_setting, size=(16, 1))],[sg.Button("追加ガチャ2"),sg.Text('ガチャ名: '+name2_setting, size=(16, 1))],[sg.Button("追加ガチャ3"),sg.Text('ガチャ名: '+name3_setting, size=(16, 1))]]
    window = sg.Window("Addition", layout, modal=True)
    choice = None

    while True:
        event, values = window.read()

        if event == "追加ガチャ1":
            open_addition1(1)
            break
        elif event == "追加ガチャ2":
            open_addition1(2)
            break
        elif event == "追加ガチャ3":
            open_addition1(3)
            break
        elif event == sg.WINDOW_CLOSED: 
            break

    window.close()


def open_addition1(num):
    ini = configparser.ConfigParser()
    if num == 1:
        ini.read('./addition1.ini','UTF-8')
    elif num == 2:
        ini.read('./addition2.ini','UTF-8')
    elif num == 3:
        ini.read('./addition3.ini','UTF-8')
    
    name_setting: str = ini.get('setting','name')
    event_setting: str = ini.get('setting','event')
    probability_setting: str = ini.get('setting','probability')
    uniform_setting: bool = is_true(ini.get('setting','uniform'))
    layout = [[sg.Text("追加設定", key="new")],[sg.Text('ガチャ名称', size=(9, 1)), sg.InputText(name_setting)],[sg.Text('事象',size=(32,1)),sg.Text('確率',size=(32,1))],[sg.Multiline(default_text=event_setting,size=(35,5)),sg.Multiline(default_text=probability_setting,size=(35,5))],[sg.Checkbox('一様分布', default=uniform_setting)],[sg.Button("Apply")]]
    window = sg.Window("Addition", layout, modal=True)
    choice = None

    while True:
        event, values = window.read()

        if event == "Apply":
            ini2 = configparser.ConfigParser()
            ini2['setting'] = {}
            ini2['setting']['name'] = str(values[0])
            ini2['setting']['event'] = str(values[1])
            ini2['setting']['probability'] = str(values[2])
            ini2['setting']['uniform'] = str(values[3])
            if num == 1:
                with open('./addition1.ini','w') as configfile:
                    ini2.write(configfile)
            elif num == 2:
                with open('./addition2.ini','w') as configfile:
                    ini2.write(configfile)
            elif num == 3:
                with open('./addition3.ini','w') as configfile:
                    ini2.write(configfile)
            break
        elif event == sg.WINDOW_CLOSED: 
            break

    window.close()
#open_setting()
#open_addition()
