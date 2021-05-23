# -*- coding: utf-8 -*-
import PySimpleGUI as sg
import os.path
import PIL.Image
import io

#  設定画面　実際には別のファイルに書いた関数を使う
def open_setting():
    layout = [[sg.Text("New Window", key="new")], [sg.Button("Exit")]]
    window = sg.Window("Settings", layout, modal=True)
    choice = None
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WINDOW_CLOSED:
            break
    window.close()

menu_def = [['設定', ['設定']]]
#  どういう形式でガチャ結果を渡すかは未定　画像の配置はどっちでやる？
weather_list = [r'img\rain.png', r'img\cloudy.png', r'img\cloudy.png', r'img\cloudy.png']
fukou_list = [r'img\rain.png', r'img\cloudy.png', r'img\cloudy.png', r'img\cloudy.png']

#  ここからレイアウトの設定　PySimpleGUIは基本的にリストのリストでレイアウトを定める
layout = [
    #  メニューバーの設定
    [sg.Menu(menu_def, tearoff=False)],
    #  map関数を使って、上で定義したパスのlistをまとめて画像のリストに変換している
    map(sg.Image, weather_list),
    map(sg.Image, fukou_list),
]
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
        open_setting()

window.close()
