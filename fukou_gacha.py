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

"""fig_dic={}
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
"""

background_img=[r"fukou_img/aozora.png",r"fukou_img/usugura.png",r"fukou_img/makkura.png"]

gacha_list=[
    ["雷に直撃します",r"fukou_img/kaminarisama.png",2],
    ["突然の雨に降られます",r"fukou_img/fashion_ame_zubunure.png",1],
    ["電車が遅延します",r"fukou_img/train_chien_man.png",1],
    ["スマホを落として画面が割れます",r"fukou_img/train_homedoor_smartphone_otosu.png",1],
    ["A判定で大学受験に落ちます",r"fukou_img/noiroze_juken_woman.png",2],
    ["Twitterのパスワードがバレます",r"fukou_img/dorobou_account_nottori.png",2],
    ["院試に合格します",r"fukou_img/juken_goukaku_daruma.png",0],
    ["AtCoderのレートが下がります",r"fukou_img/atcoder.png",1],
    ["AtCoderの色が落ちます",r"fukou_img/atcoder.png",1],
    ["AtCoderのレートが上がります",r"fukou_img/atcoder.png",0],
    ["Twitterで炎上します",r"fukou_internet_enjou_sns_woman.png",1],
    #講義関連
    ["演習の発表で炎上します",r"fukou_img/siroto.png",1],
    ["ジョルダン標準形を求めようとして計算ミスをします",r"fukou_img/school_test_enpitsu.png",1],
    ["極座標ラプラシアンを求めようとして計算ミスをします",r"fukou_img/school_test_enpitsu.png",1],
    ["卒論の発表で詰められます",r"fukou_img/mensetsu_appaku.png",1],
    ["輪講の発表で炎上します",r"fukou_img/siroto.png",1],
    ["特別講義を落として留年します",r"fukou_img/school_tani_otosu_girl.png",2],
    ["演習を落として留年します",r"fukou_img/school_tani_otosu_girl.png",2],
    ["実験を落として留年します",r"fukou_img/school_tani_otosu_girl.png",2],
    ["輪講を落として留年します",r"fukou_img/school_tani_otosu_girl.png",2],
    ["卒論着手要件を満たさず留年します",r"fukou_img/school_ryunen.png",2],
    ["卒論が書けず留年します",r"fukou_img/school_ryunen.png",2],
    ["系列別の卒業要件を満たさず留年します",r"fukou_img/school_ryunen.png",2],
    ["締切直前にLMSが落ちてレポート提出に失敗します",r"fukou_img/school_tani_otosu_girl.png",1],
    ["今学期全優上です．おめでとうございます．",r"fukou_img/100ten.png",0],
    ["GAFAに内定します．おめでとうございます．",r"fukou_img/gafa.png",0],
    ["卒論で優秀賞がもらえます．おめでとうございます．",r"fukou_img/shou.png",0],
    #院試関連
    ["院試の出願に失敗します",r"fukou_img/fugoukaku.png",2],
    ["院試の書類専攻に落ちます",r"fukou_img/fugoukaku.png",2],
    ["院試の面接で詰められます",r"fukou_img/mensetsu_appaku.png",1],
    ["院試本番で解答用紙を間違えて0点を取ります",r"fukou_img/test0.png",2],
    ["大学院の入学金を払い忘れて合格を取り消されます",r"fukou_img/money_tokeru_yen.png",2],
    #病気関連
    ["糖尿病を発症します",r"fukou_img/disease.png",2],
    ["牡蠣を食べて食中毒を発症します",r"fukou_img/disease.png",1],
    ["全身に癌ができます",r"fukou_img/disease.png",2],
    ["車にひかれて全身複雑骨折します",r"fukou_img/disease.png",2],
    ["ヤクザに撃たれて緊急手術を受けます",r"fukou_img/disease.png",2],
    ["頭を強く打って記憶喪失になります",r"fukou_img/disease.png",2]
    ]

def fukou_gacha_index():#不幸ガチャの結果を決定する関数
    size=len(gacha_list)
    num=np.random.randint(0,size)
    return num
    """if 1<=num<=10:
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
        return 7"""

def fukou_gacha():
    index=fukou_gacha_index()#乱数によってindex決定
    result_img=gacha_list[index][1]#結果の画像
    result_sentence=gacha_list[index][0]#結果の説明文

    rare=gacha_list[index][2]#不幸(1)が大不幸(2)か幸運(0)か
    background=background_img[rare]#背景画像(今のところrareで分けている)

    tweet="不幸ガチャで"#ツイートする文面
    color=""#文字の色
    if rare==1:
        tweet+="不幸:"+"「"+result_sentence+"」"+"を引きました"
        color="#ffffff"
    elif rare==2:
        tweet+="大不幸:"+"「"+result_sentence+"」"+"を引いてしまいました．．．"
        color="#ff0000"
    else:
        tweet+="あらゆる不幸を乗り越えて幸運:"+"「"+result_sentence+"」"+"を引きました!!!!"
        color="#000000"
    
    return tweet,background,[[sg.Image(result_img)],[sg.Text("ガチャ結果:"+result_sentence,text_color=color)]]
