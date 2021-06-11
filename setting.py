import PySimpleGUI as sg
import json
import numpy as np
import random

def is_true(value):
    return False if value == 'False' else bool(value)

def open_setting():
    json_open = open("./data.json","r",encoding="utf-8")
    data = json.load(json_open)
    fukou_setting:bool = is_true(data["fukou"])
    region_setting:str = data["region"]
    weather_setting:bool = is_true(data["weather"])
    trivia_setting:bool = is_true(data["trivia"])
    addition1_setting:bool = is_true(data["addition1"])
    addition2_setting:bool = is_true(data["addition2"])
    addition3_setting:bool = is_true(data["addition3"])
    json_open = open("./addition1.json","r",encoding="utf-8")
    data1 = json.load(json_open)
    name1_setting:str = data1["name"]
    json_open = open("./addition2.json","r",encoding="utf-8")
    data2 = json.load(json_open)
    name2_setting:str = data2["name"]
    json_open = open("./addition3.json","r",encoding="utf-8")
    data3 = json.load(json_open)
    name3_setting:str = data3["name"]
    values_region = ['北海道','東北','関東','中部','近畿','中国','四国','九州']
    layout = [[sg.Text("表示設定", key="new")],[sg.Checkbox('天気予報', default=weather_setting)],[sg.Text('地域', size=(4, 1)),sg.Combo(values_region, default_value=region_setting, size=(20,1)) ],[sg.Checkbox('不幸ガチャ', default=fukou_setting)],[sg.Checkbox('豆知識', default=trivia_setting)],[sg.Checkbox('追加ガチャ1: '+name1_setting, default=addition1_setting)],[sg.Checkbox('追加ガチャ2: '+name2_setting, default=addition2_setting)],[sg.Checkbox('追加ガチャ3: '+name3_setting, default=addition3_setting)],[sg.Button("Apply")]]
    window = sg.Window("Settings", layout, modal=True)
    choice = None
    while True:
        event, values = window.read()
        if event == "Apply":
            new_data = {"weather":str(values[0]),"region":str(values[1]),"fukou":str(values[2]),"trivia":str(values[3]),"addition1":str(values[4]),"addition2":str(values[5]),"addition3":str(values[6])}
            with open("./data.json","w",encoding = 'utf-8') as f:
                json.dump(new_data,f,indent=4)
            break
        elif event == sg.WINDOW_CLOSED: 
            break
    window.close()

def get_show_list():
    json_open = open("./data.json","r",encoding="utf-8")
    data = json.load(json_open)
    fukou_setting:bool = is_true(data["fukou"])
    region_setting:str = data["region"]
    weather_setting:bool = is_true(data["weather"])
    trivia_setting:bool = is_true(data["trivia"])
    addition1_setting:bool = is_true(data["addition1"])
    addition2_setting:bool = is_true(data["addition2"])
    addition3_setting:bool = is_true(data["addition3"])
    return [fukou_setting,region_setting,weather_setting,trivia_setting,addition1_setting,addition2_setting,addition3_setting]

def get_show_list_addition(num):
    if num == 1:
        json_open = open("./addition1.json","r",encoding="utf-8")
    elif num == 2:
        json_open = open("./addition2.json","r",encoding="utf-8")
    elif num == 3:
        json_open = open("./addition3.json","r",encoding="utf-8")
    
    data = json.load(json_open)
    data["event"] = data["event"].split()
    data["probability"] = data["probability"].split()
    return data
    
def open_warning():
    layout = [[sg.Text("事象と確率の個数が合っていません！！")]]
    window = sg.Window("Warning", layout, modal=True)
    choice = None
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
    window.close()


def open_addition():
    json_open = open("./addition1.json","r",encoding="utf-8")
    data1 = json.load(json_open)
    name1_setting:str = data1["name"]
    json_open = open("./addition2.json","r",encoding="utf-8")
    data2 = json.load(json_open)
    name2_setting:str = data2["name"]
    json_open = open("./addition3.json","r",encoding="utf-8")
    data3 = json.load(json_open)
    name3_setting:str = data3["name"]
    layout = [[sg.Text("追加選択", key="new")],[sg.Button("追加ガチャ1"),sg.Text('ガチャ名: '+name1_setting)],[sg.Button("追加ガチャ2"),sg.Text('ガチャ名: '+name2_setting)],[sg.Button("追加ガチャ3"),sg.Text('ガチャ名: '+name3_setting)]]
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
    if num == 1:
        json_open = open("./addition1.json","r",encoding="utf-8")
        data = json.load(json_open)
    elif num == 2:
        json_open = open("./addition2.json","r",encoding="utf-8")
        data = json.load(json_open)
    elif num == 3:
        json_open = open("./addition3.json","r",encoding="utf-8")
        data = json.load(json_open)
    
    name_setting: str = data["name"]
    event_setting: str = data["event"]
    probability_setting: str = data["probability"]
    uniform_setting: bool = is_true(data["uniform"])
    layout = [[sg.Text("追加設定", key="new")],[sg.Text('ガチャ名称', size=(9, 1)), sg.InputText(name_setting)],[sg.Text('事象',size=(32,1)),sg.Text('確率',size=(32,1))],[sg.Multiline(default_text=event_setting,size=(35,5)),sg.Multiline(default_text=probability_setting,size=(35,5))],[sg.Checkbox('一様分布', default=uniform_setting)],[sg.Button("Apply")]]
    window = sg.Window("Addition", layout, modal=True)
    choice = None

    while True:
        event, values = window.read()

        if event == "Apply":
            new_data = {"name":str(values[0]),"event":str(values[1]),"probability":str(values[2]),"uniform":str(values[3])}
            if (len(new_data["event"].split()) != len(new_data["probability"].split())) and new_data["uniform"] != "True":
                open_warning()
            elif num == 1:
                with open("./addition1.json","w",encoding = 'utf-8') as f:
                    json.dump(new_data,f,indent=4)
                break
            elif num == 2:
                with open("./addition2.json","w",encoding = 'utf-8') as f:
                    json.dump(new_data,f,indent=4)
                break
            elif num == 3:
                with open("./addition3.json","w",encoding = 'utf-8') as f:
                    json.dump(new_data,f,indent=4)
                break
        elif event == sg.WINDOW_CLOSED: 
            break

    window.close()

def get_addition_result(num):
    if num == 1:
        json_open = open("./addition1.json","r",encoding="utf-8")
        data = json.load(json_open)
    elif num == 2:
        json_open = open("./addition2.json","r",encoding="utf-8")
        data = json.load(json_open)
    elif num == 3:
        json_open = open("./addition3.json","r",encoding="utf-8")
        data = json.load(json_open)

    name_setting: str = data["name"]
    event_setting: str = data["event"].split()
    probability_setting: float = data["probability"].split()
    uniform_setting: bool = is_true(data["uniform"])

    len_event = len(event_setting)
    sum = 0.0
    
    if uniform_setting == 1:
        probability_setting = [p/float(len_event) for p in np.ones(len_event)]
    else:
        for i in range(len_event):
            probability_setting[i] = float(probability_setting[i])
            sum = sum + probability_setting[i]
        probability_setting = [p/sum for p in probability_setting]
    #print(probability_setting)
    p = 0.0
    i = -1
    ran = random.random()
    #print(ran)
    while p < ran:
        i = i + 1
        p = p + probability_setting[i]
        #print(p)
        if i == len_event - 1:
            break

    #print(event_setting[i])
    
    

    return name_setting+"の結果は"+event_setting[i]+"でした","path",[
    [sg.Text(name_setting,font=('Noto Serif CJK JP',20)),sg.Text("の結果",font=('Noto Serif CJK JP',10))],
    [sg.Text("「"+event_setting[i]+"」",font=('Noto Serif CJK JP',30))],
    [sg.Button("Close")]
    ]


def show_test():
    tweet,path,layout = get_addition_result(2)
    window = sg.Window("Addition", layout, modal=True)
    choice = None
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        if event == "Close":
            break
    window.close()


#get_addition_result(1)
#show_test()
