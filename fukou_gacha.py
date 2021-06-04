"""
使い方
import fukou_gacha
を先頭に書いて

fukou_gacha.fukou_gacha()
とすれば結果の画像と説明文をそれぞれsg.Image,sg.Textのリストに変換したものが返ってくる
一行目に結果の画像、二行目に結果の説明文が表示される
"""

import numpy as np
import os
import PySimpleGUI as sg

fig_dic={}
fig_dic[1]=r"img/kaminarisama.png"
fig_dic[2]=r"img/fashion_ame_zubunure.png"
fig_dic[3]=r"img/train_chien_man.png"
fig_dic[4]=r"img/train_homedoor_smartphone_otosu.png"
fig_dic[5]=r"img/noiroze_juken_woman.png"
fig_dic[6]=r"img/dorobou_account_nottori.png"
fig_dic[7]=r"img/juken_goukaku_daruma.png"

result_dic={}
result_dic[1]="雷に直撃します"
result_dic[2]="突然の雨に降られます"
result_dic[3]="電車が遅延します"
result_dic[4]="スマホを落として画面が割れます"
result_dic[5]="A判定で大学受験に落ちます"
result_dic[6]="Twitterのパスワードがバレます"
result_dic[7]="あらゆる不幸を乗り越え院試に合格します"

def fukou_gacha_index():#不幸ガチャの結果を決定する関数
    num=np.random.randint(1,101)
    if 1<=num<=10:
        return 1
    elif num<=20:
        return 2
    elif num<=30:
        return 3
    elif num<=40:
        return 4
    elif num<=50:
        return 5
    elif num<=55:
        return 6
    else:
        return 7

def fukou_gacha():
    index=fukou_gacha_index()#乱数によってindex決定
    result_img=fig_dic[index]#結果の画像
    result_sentence=result_dic[index]#結果の説明文
    return [[sg.Image(result_img)],[sg.Text("ガチャ結果:"+result_sentence)]]

