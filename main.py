# -*- coding: utf-8 -*-
import PySimpleGUI as sg
import os.path
import PIL.Image
import io
import setting

#  設定画面　実際には別のファイルに書いた関数を使う


#def get_show_list():
#    return [True, False]

def get_weather_list():
    return [r'img\rain.png', r'img\cloudy.png', r'img\cloudy.png', r'img\cloudy.png']

def get_fukou_list():
    return [r'img\rain.png', r'img\rain.png', r'img\rain.png', r'img\cloudy.png']

menu_def = [['設定', ['設定','追加']]]
#  どういう形式でガチャ結果を渡すかは未定　画像の配置はどっちでやる？
weather_list = get_weather_list()
fukou_list = get_fukou_list()

#  どのガチャを表示されるか
show_list = setting.get_show_list()
Y_weather: bool = show_list[0]
Y_Fukou: bool = show_list[2]

#  ここからレイアウトの設定　PySimpleGUIは基本的にリストのリストでレイアウトを定める
layout = [
    #  メニューバーの設定
    [sg.Menu(menu_def, tearoff=False)],
]
#  show_listの対応する成分がTrueなら、レイアウトに加える（Falseの場合も全体のレイアウトを保つ方法はまだわかってない
if(Y_weather):
    #  map関数を使って、上で定義したパスのlistをまとめて画像のリストに変換している
    layout.append(map(sg.Image, weather_list))
if(Y_Fukou):
    layout.append(map(sg.Image, fukou_list))
#  ここまで

#  ウィンドウのタイトル
window = sg.Window('Random Gacha', layout)

while True:
    event, values = window.read()
    #  xボタンが押されたら閉じる
    if event == sg.WINDOW_CLOSED:
        break
    #  メニューバーの「設定」が押されたら設定画面を開く
    if event == '設定':
        setting.open_setting()
    if event == '追加':
        setting.open_addition()

window.close()
