# -*- coding: utf-8 -*-
import PySimpleGUI as sg
import os.path
import PIL.Image
import io
import setting
import weather_prediction
import mamechishiki
import webbrowser
import fukou_gacha

menu_def = [['設定', ['設定','追加']]]

#  どのガチャを表示されるか
show_list = setting.get_show_list()
Y_weather: bool = show_list[0]
Y_Fukou: bool = show_list[2]

#  ここからレイアウトの設定　PySimpleGUIは基本的にリストのリストでレイアウトを定める
#  各ボタンを押したときに実行される関数
#  引数に、各々が実装してくれた関数と、そのガチャのウィンドウのタイトルを渡す
#  関数の返り値は、各ウィンドウのレイアウトを定めるリストのリスト
#  背景画像についてはまだ実装していない
#  3番目の返り値でツイートする文字列を返す
def open_window(Func, title, tweet = 'test'):
    _layout = Func()
    _layout.append([sg.Button("ツイート", key="tweet", size=(50, 5))])
    url = 'https://twitter.com/intent/tweet?text='
    url += tweet
    _window = sg.Window(title, _layout, modal=True)
    choice = None
    while True:
        _event, _values = _window.read()
        if _event == "Exit" or _event == sg.WIN_CLOSED:
            break
        if _event == "tweet":
            webbrowser.open(url)

    _window.close()

layout = [
    #  メニューバーの設定
    [sg.Menu(menu_def, tearoff=False)],
    [sg.Button("天気予報を見る", key="weather", size=(50, 5))],
    [sg.Button("不幸ガチャ", key="fukou", size=(50, 5))],
    mamechishiki.get_mamechishiki_list()
]

#  ウィンドウのタイトル
window = sg.Window('Random Gacha', layout, size=(750, 500))

while True:
    event, values = window.read()
    if event.startswith("URL "):
        url = event.split(' ')[1]
        webbrowser.open(url)
    #  xボタンが押されたら閉じる
    if event == sg.WINDOW_CLOSED:
        break
    #  メニューバーの「設定」が押されたら設定画面を開く
    if event == '設定':
        setting.open_setting()
    if event == '追加':
        setting.open_addition()
    if event == 'weather':
        open_window(weather_prediction.return_weather, "天気ガチャ")
    if event == 'fukou':
        open_window(fukou_gacha.fukou_gacha, "不幸ガチャ")
    if event == 'tweet':
        url = 'https://twitter.com/intent/tweet?text=Insert Text Here'
        webbrowser.open(url)

window.close()
