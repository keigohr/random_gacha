"""
使い方
import insi_gacha
を先頭に書いて

insi_gacha.insi_gacha()
とすれば結果の画像と説明文をそれぞれsg.Image,sg.Textのリストに変換したものが返ってくる
一行目に結果の画像、二行目に結果の説明文が表示される
"""


import numpy as np
import os
import PySimpleGUI as sg


gacha_list=[
    [#ハズレ枠
        ["口頭試問で教員に質問詰めにされる",r"insi_img/mensetsu_appaku.png","%E9%99%A2%E8%A9%A6%E3%82%AC%E3%83%81%E3%83%A3%E3%81%A7%E3%83%8F%E3%82%BA%E3%83%AC%E3%80%8C%E5%8F%A3%E9%A0%AD%E8%A9%A6%E5%95%8F%E3%81%A7%E6%95%99%E5%93%A1%E3%81%AB%E8%B3%AA%E5%95%8F%E8%A9%B0%E3%82%81%E3%81%AB%E3%81%95%E3%82%8C%E3%82%8B%E3%80%8D%E3%82%92%E5%BC%95%E3%81%8D%E3%81%BE%E3%81%97%E3%81%9F"],
        ["テスト本番で受験票を忘れる",r"insi_img/illustrain02-juken09.png","%E9%99%A2%E8%A9%A6%E3%82%AC%E3%83%81%E3%83%A3%E3%81%A7%E3%83%8F%E3%82%BA%E3%83%AC%E3%80%8C%E3%83%86%E3%82%B9%E3%83%88%E6%9C%AC%E7%95%AA%E3%81%A7%E5%8F%97%E9%A8%93%E7%A5%A8%E3%82%92%E5%BF%98%E3%82%8C%E3%82%8B%E3%80%8D%E3%82%92%E5%BC%95%E3%81%8D%E3%81%BE%E3%81%97%E3%81%9F"],
        ["テスト本番で筆記用具が故障する",r"insi_img/seizu_pen.png","%E9%99%A2%E8%A9%A6%E3%82%AC%E3%83%81%E3%83%A3%E3%81%A7%E3%83%8F%E3%82%BA%E3%83%AC%E3%80%8C%E3%83%86%E3%82%B9%E3%83%88%E6%9C%AC%E7%95%AA%E3%81%A7%E7%AD%86%E8%A8%98%E7%94%A8%E5%85%B7%E3%81%8C%E6%95%85%E9%9A%9C%E3%81%99%E3%82%8B%E3%80%8D%E3%82%92%E5%BC%95%E3%81%8D%E3%81%BE%E3%81%97%E3%81%9F"],
        ["試験当日に電車が遅延",r"insi_img/train_chien_man.png","%E9%99%A2%E8%A9%A6%E3%82%AC%E3%83%81%E3%83%A3%E3%81%A7%E3%83%8F%E3%82%BA%E3%83%AC%E3%80%8C%E8%A9%A6%E9%A8%93%E5%BD%93%E6%97%A5%E3%81%AB%E9%9B%BB%E8%BB%8A%E3%81%8C%E9%81%85%E5%BB%B6%E3%80%8D%E3%82%92%E5%BC%95%E3%81%8D%E3%81%BE%E3%81%97%E3%81%9F"],
        ["試験本番で解答用紙を間違える",r"insi_img/test0.png","%E9%99%A2%E8%A9%A6%E3%82%AC%E3%83%81%E3%83%A3%E3%81%A7%E3%83%8F%E3%82%BA%E3%83%AC%E3%80%8C%E8%A9%A6%E9%A8%93%E6%9C%AC%E7%95%AA%E3%81%A7%E8%A7%A3%E7%AD%94%E7%94%A8%E7%B4%99%E3%82%92%E9%96%93%E9%81%95%E3%81%88%E3%82%8B%E3%80%8D%E3%82%92%E5%BC%95%E3%81%8D%E3%81%BE%E3%81%97%E3%81%9F"],
        ["試験時間中に携帯が鳴って怒られる",r"insi_img/smartphone_vibration.png","%E9%99%A2%E8%A9%A6%E3%82%AC%E3%83%81%E3%83%A3%E3%81%A7%E3%83%8F%E3%82%BA%E3%83%AC%E3%80%8C%E8%A9%A6%E9%A8%93%E6%99%82%E9%96%93%E4%B8%AD%E3%81%AB%E6%90%BA%E5%B8%AF%E3%81%8C%E9%B3%B4%E3%81%A3%E3%81%A6%E6%80%92%E3%82%89%E3%82%8C%E3%82%8B%E3%80%8D%E3%82%92%E5%BC%95%E3%81%8D%E3%81%BE%E3%81%97%E3%81%9F"],
        ["試験当日に風邪をひく",r"insi_img/sick_guai_warui_man.png","%E9%99%A2%E8%A9%A6%E3%82%AC%E3%83%81%E3%83%A3%E3%81%A7%E3%83%8F%E3%82%BA%E3%83%AC%E3%80%8C%E8%A9%A6%E9%A8%93%E5%BD%93%E6%97%A5%E3%81%AB%E9%A2%A8%E9%82%AA%E3%82%92%E3%81%B2%E3%81%8F%E3%80%8D%E3%82%92%E5%BC%95%E3%81%8D%E3%81%BE%E3%81%97%E3%81%9F"],
        ["夏院試に落ちて冬院試に突入",r"insi_img/school_samui_seifuku.png","%E9%99%A2%E8%A9%A6%E3%82%AC%E3%83%81%E3%83%A3%E3%81%A7%E3%83%8F%E3%82%BA%E3%83%AC%E3%80%8C%E5%A4%8F%E9%99%A2%E8%A9%A6%E3%81%AB%E8%90%BD%E3%81%A1%E3%81%A6%E5%86%AC%E9%99%A2%E8%A9%A6%E3%81%AB%E7%AA%81%E5%85%A5%E3%80%8D%E3%82%92%E5%BC%95%E3%81%8D%E3%81%BE%E3%81%97%E3%81%9F"]
    ],
    #大ハズレ枠
    [
        ["出願課題の出来が悪く足切り",r"insi_img/document_shinsa_fugoukaku_kadai.png","%E9%99%A2%E8%A9%A6%E3%82%AC%E3%83%81%E3%83%A3%E3%81%A7%E5%A4%A7%E3%83%8F%E3%82%BA%E3%83%AC%E3%80%8C%E5%87%BA%E9%A1%98%E8%AA%B2%E9%A1%8C%E3%81%AE%E5%87%BA%E6%9D%A5%E3%81%8C%E6%82%AA%E3%81%8F%E8%B6%B3%E5%88%87%E3%82%8A%E3%80%8D%E3%82%92%E5%BC%95%E3%81%8D%E3%81%BE%E3%81%97%E3%81%9F"],
        ["TOEFLの点数で足切りされる",r"insi_img/document_shinsa_fugoukaku_toefl.png","%E9%99%A2%E8%A9%A6%E3%82%AC%E3%83%81%E3%83%A3%E3%81%A7%E5%A4%A7%E3%83%8F%E3%82%BA%E3%83%AC%E3%80%8CTOEFL%E3%81%AE%E7%82%B9%E6%95%B0%E3%81%A7%E8%B6%B3%E5%88%87%E3%82%8A%E3%81%95%E3%82%8C%E3%82%8B%E3%80%8D%E3%82%92%E5%BC%95%E3%81%8D%E3%81%BE%E3%81%97%E3%81%9F"],
        ["学部の成績不良で足切りされる",r"insi_img/document_shinsa_fugoukaku_seiseki.png","%E9%99%A2%E8%A9%A6%E3%82%AC%E3%83%81%E3%83%A3%E3%81%A7%E5%A4%A7%E3%83%8F%E3%82%BA%E3%83%AC%E3%80%8C%E5%AD%A6%E9%83%A8%E3%81%AE%E6%88%90%E7%B8%BE%E4%B8%8D%E8%89%AF%E3%81%A7%E8%B6%B3%E5%88%87%E3%82%8A%E3%81%95%E3%82%8C%E3%82%8B%E3%80%8D%E3%82%92%E5%BC%95%E3%81%8D%E3%81%BE%E3%81%97%E3%81%9F"],
        ["共通数学で爆死して不合格",r"insi_img/noiroze_juken_man.png","%E9%99%A2%E8%A9%A6%E3%82%AC%E3%83%81%E3%83%A3%E3%81%A7%E5%A4%A7%E3%83%8F%E3%82%BA%E3%83%AC%E3%80%8C%E5%85%B1%E9%80%9A%E6%95%B0%E5%AD%A6%E3%81%A7%E7%88%86%E6%AD%BB%E3%81%97%E3%81%A6%E4%B8%8D%E5%90%88%E6%A0%BC%E3%80%8D%E3%82%92%E5%BC%95%E3%81%8D%E3%81%BE%E3%81%97%E3%81%9F"],
        ["専門科目レポートが書き終わらず不合格",r"insi_img/shimekiri_report_hakui_man.png","%E9%99%A2%E8%A9%A6%E3%82%AC%E3%83%81%E3%83%A3%E3%81%A7%E5%A4%A7%E3%83%8F%E3%82%BA%E3%83%AC%E3%80%8C%E5%B0%82%E9%96%80%E7%A7%91%E7%9B%AE%E3%83%AC%E3%83%9D%E3%83%BC%E3%83%88%E3%81%8C%E6%9B%B8%E3%81%8D%E7%B5%82%E3%82%8F%E3%82%89%E3%81%9A%E4%B8%8D%E5%90%88%E6%A0%BC%E3%80%8D%E3%82%92%E5%BC%95%E3%81%8D%E3%81%BE%E3%81%97%E3%81%9F"],
        ["専門科目レポートの出し忘れで不合格",r"insi_img/document_report.png","%E9%99%A2%E8%A9%A6%E3%82%AC%E3%83%81%E3%83%A3%E3%81%A7%E5%A4%A7%E3%83%8F%E3%82%BA%E3%83%AC%E3%80%8C%E5%B0%82%E9%96%80%E7%A7%91%E7%9B%AE%E3%83%AC%E3%83%9D%E3%83%BC%E3%83%88%E3%81%AE%E5%87%BA%E3%81%97%E5%BF%98%E3%82%8C%E3%81%A7%E4%B8%8D%E5%90%88%E6%A0%BC%E3%80%8D%E3%82%92%E5%BC%95%E3%81%8D%E3%81%BE%E3%81%97%E3%81%9F"],
        ["解答用紙に名前を書き忘れ不合格",r"insi_img/test0_namae.png","%E9%99%A2%E8%A9%A6%E3%82%AC%E3%83%81%E3%83%A3%E3%81%A7%E5%A4%A7%E3%83%8F%E3%82%BA%E3%83%AC%E3%80%8C%E8%A7%A3%E7%AD%94%E7%94%A8%E7%B4%99%E3%81%AB%E5%90%8D%E5%89%8D%E3%82%92%E6%9B%B8%E3%81%8D%E5%BF%98%E3%82%8C%E4%B8%8D%E5%90%88%E6%A0%BC%E3%80%8D%E3%82%92%E5%BC%95%E3%81%8D%E3%81%BE%E3%81%97%E3%81%9F"],
        ["合格するも入学金の払い忘れで合格取り消し",r"insi_img/money_tokeru_yen.png","%E9%99%A2%E8%A9%A6%E3%82%AC%E3%83%81%E3%83%A3%E3%81%A7%E5%A4%A7%E3%83%8F%E3%82%BA%E3%83%AC%E3%80%8C%E5%90%88%E6%A0%BC%E3%81%99%E3%82%8B%E3%82%82%E5%85%A5%E5%AD%A6%E9%87%91%E3%81%AE%E6%89%95%E3%81%84%E5%BF%98%E3%82%8C%E3%81%A7%E5%90%88%E6%A0%BC%E5%8F%96%E3%82%8A%E6%B6%88%E3%81%97%E3%80%8D%E3%82%92%E5%BC%95%E3%81%8D%E3%81%BE%E3%81%97%E3%81%9F"],
        ["出願書類に不備があり不合格",r"insi_img/document_shinsa_fugoukaku_fubi.png","%E9%99%A2%E8%A9%A6%E3%82%AC%E3%83%81%E3%83%A3%E3%81%A7%E5%A4%A7%E3%83%8F%E3%82%BA%E3%83%AC%E3%80%8C%E5%87%BA%E9%A1%98%E6%9B%B8%E9%A1%9E%E3%81%AB%E4%B8%8D%E5%82%99%E3%81%8C%E3%81%82%E3%82%8A%E4%B8%8D%E5%90%88%E6%A0%BC%E3%80%8D%E3%82%92%E5%BC%95%E3%81%8D%E3%81%BE%E3%81%97%E3%81%9F"],
        ["合格するも卒論が書ききれず留年",r"insi_img/school_sotsuron_shimekiri_woman.png","%E9%99%A2%E8%A9%A6%E3%82%AC%E3%83%81%E3%83%A3%E3%81%A7%E5%A4%A7%E3%83%8F%E3%82%BA%E3%83%AC%E3%80%8C%E5%90%88%E6%A0%BC%E3%81%99%E3%82%8B%E3%82%82%E5%8D%92%E8%AB%96%E3%81%8C%E6%9B%B8%E3%81%8D%E3%81%8D%E3%82%8C%E3%81%9A%E7%95%99%E5%B9%B4%E3%80%8D%E3%82%92%E5%BC%95%E3%81%8D%E3%81%BE%E3%81%97%E3%81%9F"],
        ["試験当日にコロナを発症して受験不可となる",r"insi_img/virus_corona.png","%E9%99%A2%E8%A9%A6%E3%82%AC%E3%83%81%E3%83%A3%E3%81%A7%E5%A4%A7%E3%83%8F%E3%82%BA%E3%83%AC%E3%80%8C%E8%A9%A6%E9%A8%93%E5%BD%93%E6%97%A5%E3%81%AB%E3%82%B3%E3%83%AD%E3%83%8A%E3%82%92%E7%99%BA%E7%97%87%E3%81%97%E3%81%A6%E5%8F%97%E9%A8%93%E4%B8%8D%E5%8F%AF%E3%81%A8%E3%81%AA%E3%82%8B%E3%80%8D%E3%82%92%E5%BC%95%E3%81%8D%E3%81%BE%E3%81%97%E3%81%9F"]
    ],
    #当たり枠
    [
        ["第一志望の研究室に合格",r"insi_img/medal1.png","%E9%99%A2%E8%A9%A6%E3%82%AC%E3%83%81%E3%83%A3%E3%81%A7%E3%82%A2%E3%82%BF%E3%83%AA%E3%80%8C%E7%AC%AC%E4%B8%80%E5%BF%97%E6%9C%9B%E3%81%AE%E7%A0%94%E7%A9%B6%E5%AE%A4%E3%81%AB%E5%90%88%E6%A0%BC%E3%80%8D%E3%82%92%E5%BC%95%E3%81%8D%E3%81%BE%E3%81%97%E3%81%9F"],
        ["第二志望の研究室に合格",r"insi_img/medal2.png","%E9%99%A2%E8%A9%A6%E3%82%AC%E3%83%81%E3%83%A3%E3%81%A7%E3%82%A2%E3%82%BF%E3%83%AA%E3%80%8C%E7%AC%AC%E4%BA%8C%E5%BF%97%E6%9C%9B%E3%81%AE%E7%A0%94%E7%A9%B6%E5%AE%A4%E3%81%AB%E5%90%88%E6%A0%BC%E3%80%8D%E3%82%92%E5%BC%95%E3%81%8D%E3%81%BE%E3%81%97%E3%81%9F"],
        ["第三志望の研究室に合格",r"insi_img/medal3.png","%E9%99%A2%E8%A9%A6%E3%82%AC%E3%83%81%E3%83%A3%E3%81%A7%E3%82%A2%E3%82%BF%E3%83%AA%E3%80%8C%E7%AC%AC%E4%B8%89%E5%BF%97%E6%9C%9B%E3%81%AE%E7%A0%94%E7%A9%B6%E5%AE%A4%E3%81%AB%E5%90%88%E6%A0%BC%E3%80%8D%E3%82%92%E5%BC%95%E3%81%8D%E3%81%BE%E3%81%97%E3%81%9F"],
        ["共通数学で満点を獲得",r"insi_img/100ten_kyotu.png","%E9%99%A2%E8%A9%A6%E3%82%AC%E3%83%81%E3%83%A3%E3%81%A7%E3%82%A2%E3%82%BF%E3%83%AA%E3%80%8C%E5%85%B1%E9%80%9A%E6%95%B0%E5%AD%A6%E3%81%A7%E6%BA%80%E7%82%B9%E3%82%92%E7%8D%B2%E5%BE%97%E3%80%8D%E3%82%92%E5%BC%95%E3%81%8D%E3%81%BE%E3%81%97%E3%81%9F"],
        ["院試レポートで満点を獲得",r"insi_img/100ten_report.png","%E9%99%A2%E8%A9%A6%E3%82%AC%E3%83%81%E3%83%A3%E3%81%A7%E3%82%A2%E3%82%BF%E3%83%AA%E3%80%8C%E9%99%A2%E8%A9%A6%E3%83%AC%E3%83%9D%E3%83%BC%E3%83%88%E3%81%A7%E6%BA%80%E7%82%B9%E3%82%92%E7%8D%B2%E5%BE%97%E3%80%8D%E3%82%92%E5%BC%95%E3%81%8D%E3%81%BE%E3%81%97%E3%81%9F"],
        ["本命に落ちるも併願で合格",r"insi_img/juken_goukakuhappyou_happy_heigan.png","%E9%99%A2%E8%A9%A6%E3%82%AC%E3%83%81%E3%83%A3%E3%81%A7%E3%82%A2%E3%82%BF%E3%83%AA%E3%80%8C%E6%9C%AC%E5%91%BD%E3%81%AB%E8%90%BD%E3%81%A1%E3%82%8B%E3%82%82%E4%BD%B5%E9%A1%98%E3%81%A7%E5%90%88%E6%A0%BC%E3%80%8D%E3%82%92%E5%BC%95%E3%81%8D%E3%81%BE%E3%81%97%E3%81%9F"],
        ["夏院試に落ちるも冬院試で合格",r"insi_img/juken_goukakuhappyou_happy_fuyu.png","%E9%99%A2%E8%A9%A6%E3%82%AC%E3%83%81%E3%83%A3%E3%81%A7%E3%82%A2%E3%82%BF%E3%83%AA%E3%80%8C%E5%A4%8F%E9%99%A2%E8%A9%A6%E3%81%AB%E8%90%BD%E3%81%A1%E3%82%8B%E3%82%82%E5%86%AC%E9%99%A2%E8%A9%A6%E3%81%A7%E5%90%88%E6%A0%BC%E3%80%8D%E3%82%92%E5%BC%95%E3%81%8D%E3%81%BE%E3%81%97%E3%81%9F"]
    ]
]



def insi_gacha_index():
    rare=np.random.randint(0,100)
    rarity=-1
    if 0<=rare<=60:
        rarity=0
        #ハズレ
    elif rare<=90:
        rarity=1
        #大はずれ
    else:
        rarity=2
        #当たり
    size=len(gacha_list[rarity])
    index=np.random.randint(0,size)

    return rarity, index
    
def insi_gacha():
    rarity_index,index=insi_gacha_index()

    result_sentence=gacha_list[rarity_index][index][0]
    result_image=gacha_list[rarity_index][index][1]
    result_tweet=gacha_list[rarity_index][index][2]

    rarity=""
    background_color=""
    sentence_color=""
    result_font=""
    background_color_image=""
    if rarity_index==0:
        rarity="ハズレ"
        background_color="DarkGrey"
        background_color_image="#a9a9a9"
        sentence_color="#000000"
    elif rarity_index==1:
        rarity="大ハズレ"
        background_color="Black"
        background_color_image="#000000"
        sentence_color="#ff0000"
    else:
        rarity="あたり"
        background_color="LightYellow"
        background_color_image="#ffffe0"
        sentence_color="#000000"
    return result_tweet,background_color,[[sg.Image(result_image,background_color=background_color_image)]]
