import numpy as np
import os
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

def fukou_gacha_fig(result):#不幸ガチャの結果の画像を返す関数
    fig_dic={}
    fig_dic[1]=r"img/kaminarisama.png"
    fig_dic[2]=r"img/fashion_ame_zubunure.png"
    fig_dic[3]=r"img/train_chien_man.png"
    fig_dic[4]=r"img/train_homedoor_smartphone_otosu.png"
    fig_dic[5]=r"img/noiroze_juken_woman.png"
    fig_dic[6]=r"img/dorobou_account_nottori.png"
    fig_dic[7]=r"img/juken_goukaku_daruma.png"
    return [fig_dic[result]]

def fukou_gacha_sentence(result):#ガチャ結果の説明及び豆知識の文章を返す関数
    result_dic={}
    result_dic[1]="雷に直撃します"
    result_dic[2]="突然の雨に降られます"
    result_dic[3]="電車が遅延します"
    result_dic[4]="スマホを落として画面が割れます"
    result_dic[5]="A判定で大学受験に落ちます"
    result_dic[6]="Twitterのパスワードがバレます"
    result_dic[7]="あらゆる不幸を乗り越え院試に合格します"
    return result_dic[result]

