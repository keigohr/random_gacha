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
        ["口頭試問で教員に質問詰めにされます",r"insi_img/mensetsu_appaku.png","%E9%99%A2%E8%A9%A6%E3%82%AC%E3%83%81%E3%83%A3%E3%81%A7%E3%83%8F%E3%82%BA%E3%83%AC%3A%E3%80%8C%E5%8F%A3%E9%A0%AD%E8%A9%A6%E5%95%8F%E3%81%A7%E6%95%99%E5%93%A1%E3%81%AB%E8%B3%AA%E5%95%8F%E8%A9%B0%E3%82%81%E3%81%AB%E3%81%95%E3%82%8C%E3%81%BE%E3%81%99%E3%80%8D%E3%82%92%E5%BC%95%E3%81%8D%E3%81%BE%E3%81%97%E3%81%9F"],
        ["テスト本番で受験票を忘れます",r"insi_img/illustrain02-juken09.png","%E9%99%A2%E8%A9%A6%E3%82%AC%E3%83%81%E3%83%A3%E3%81%A7%E3%83%8F%E3%82%BA%E3%83%AC%3A%E3%80%8C%E3%83%86%E3%82%B9%E3%83%88%E6%9C%AC%E7%95%AA%E3%81%A7%E5%8F%97%E9%A8%93%E7%A5%A8%E3%82%92%E5%BF%98%E3%82%8C%E3%81%BE%E3%81%99%E3%80%8D%E3%82%92%E5%BC%95%E3%81%8D%E3%81%BE%E3%81%97%E3%81%9F"],
        ["テスト本番で消しゴムを忘れます",r"insi_img/bunbougu_keshigomu.png","%E9%99%A2%E8%A9%A6%E3%82%AC%E3%83%81%E3%83%A3%E3%81%A7%E3%83%8F%E3%82%BA%E3%83%AC%3A%E3%80%8C%E3%83%86%E3%82%B9%E3%83%88%E6%9C%AC%E7%95%AA%E3%81%A7%E6%B6%88%E3%81%97%E3%82%B4%E3%83%A0%E3%82%92%E5%BF%98%E3%82%8C%E3%81%BE%E3%81%99%E3%80%8D%E3%82%92%E5%BC%95%E3%81%8D%E3%81%BE%E3%81%97%E3%81%9F"],
        ["テスト本番で筆記用具が故障します",r"insi_img/seizu_pen.png","%E9%99%A2%E8%A9%A6%E3%82%AC%E3%83%81%E3%83%A3%E3%81%A7%E3%83%8F%E3%82%BA%E3%83%AC%3A%E3%80%8C%E3%83%86%E3%82%B9%E3%83%88%E6%9C%AC%E7%95%AA%E3%81%A7%E7%AD%86%E8%A8%98%E7%94%A8%E5%85%B7%E3%81%8C%E6%95%85%E9%9A%9C%E3%81%97%E3%81%BE%E3%81%99%E3%80%8D%E3%82%92%E5%BC%95%E3%81%8D%E3%81%BE%E3%81%97%E3%81%9F"],
        ["志望の低い研究室に配属されます",r"insi_img/456.png","%E9%99%A2%E8%A9%A6%E3%82%AC%E3%83%81%E3%83%A3%E3%81%A7%E3%83%8F%E3%82%BA%E3%83%AC%3A%E3%80%8C%E7%AC%AC%E5%9B%9B%E5%BF%97%E6%9C%9B%E3%81%AE%E7%A0%94%E7%A9%B6%E5%AE%A4%E3%81%AB%E9%85%8D%E5%B1%9E%E3%81%95%E3%82%8C%E3%81%BE%E3%81%99%E3%80%8D%E3%82%92%E5%BC%95%E3%81%8D%E3%81%BE%E3%81%97%E3%81%9F"],
        #"""["第五志望の研究室に配属されます","%E9%99%A2%E8%A9%A6%E3%82%AC%E3%83%81%E3%83%A3%E3%81%A7%E3%83%8F%E3%82%BA%E3%83%AC%3A%E3%80%8C%E7%AC%AC%E4%BA%94%E5%BF%97%E6%9C%9B%E3%81%AE%E7%A0%94%E7%A9%B6%E5%AE%A4%E3%81%AB%E9%85%8D%E5%B1%9E%E3%81%95%E3%82%8C%E3%81%BE%E3%81%99%E3%80%8D%E3%82%92%E5%BC%95%E3%81%8D%E3%81%BE%E3%81%97%E3%81%9F"],
        #["第六志望の研究室に配属されます","%E9%99%A2%E8%A9%A6%E3%82%AC%E3%83%81%E3%83%A3%E3%81%A7%E3%83%8F%E3%82%BA%E3%83%AC%3A%E3%80%8C%E7%AC%AC%E5%85%AD%E5%BF%97%E6%9C%9B%E3%81%AE%E7%A0%94%E7%A9%B6%E5%AE%A4%E3%81%AB%E9%85%8D%E5%B1%9E%E3%81%95%E3%82%8C%E3%81%BE%E3%81%99%E3%80%8D%E3%82%92%E5%BC%95%E3%81%8D%E3%81%BE%E3%81%97%E3%81%9F"],"""
        ["試験当日に電車が遅延します",r"insi_img/train_chien_man.png","%E9%99%A2%E8%A9%A6%E3%82%AC%E3%83%81%E3%83%A3%E3%81%A7%E3%83%8F%E3%82%BA%E3%83%AC%3A%E3%80%8C%E8%A9%A6%E9%A8%93%E5%BD%93%E6%97%A5%E3%81%AB%E9%9B%BB%E8%BB%8A%E3%81%8C%E9%81%85%E5%BB%B6%E3%81%97%E3%81%BE%E3%81%99%E3%80%8D%E3%82%92%E5%BC%95%E3%81%8D%E3%81%BE%E3%81%97%E3%81%9F"],
        ["試験本番で解答用紙を間違えます",r"insi_img/school_test_enpitsu.png","%E9%99%A2%E8%A9%A6%E3%82%AC%E3%83%81%E3%83%A3%E3%81%A7%E3%83%8F%E3%82%BA%E3%83%AC%3A%E3%80%8C%E8%A9%A6%E9%A8%93%E6%9C%AC%E7%95%AA%E3%81%A7%E8%A7%A3%E7%AD%94%E7%94%A8%E7%B4%99%E3%82%92%E9%96%93%E9%81%95%E3%81%88%E3%81%BE%E3%81%99%E3%80%8D%E3%82%92%E5%BC%95%E3%81%8D%E3%81%BE%E3%81%97%E3%81%9F"],
        ["試験時間中に携帯の通知音が鳴り怒られます",r"insi_img/smartphone_vibration.png","%E9%99%A2%E8%A9%A6%E3%82%AC%E3%83%81%E3%83%A3%E3%81%A7%E3%83%8F%E3%82%BA%E3%83%AC%3A%E3%80%8C%E8%A9%A6%E9%A8%93%E6%99%82%E9%96%93%E4%B8%AD%E3%81%AB%E6%90%BA%E5%B8%AF%E3%81%AE%E9%80%9A%E7%9F%A5%E9%9F%B3%E3%81%8C%E9%B3%B4%E3%82%8A%E6%80%92%E3%82%89%E3%82%8C%E3%81%BE%E3%81%99%E3%80%8D%E3%82%92%E5%BC%95%E3%81%8D%E3%81%BE%E3%81%97%E3%81%9F"],
        ["試験本番に熱を出します",r"insi_img/sick_guai_warui_man.png","%E9%99%A2%E8%A9%A6%E3%82%AC%E3%83%81%E3%83%A3%E3%81%A7%E3%83%8F%E3%82%BA%E3%83%AC%3A%E3%80%8C%E8%A9%A6%E9%A8%93%E6%9C%AC%E7%95%AA%E3%81%AB%E7%86%B1%E3%82%92%E5%87%BA%E3%81%97%E3%81%BE%E3%81%99%E3%80%8D%E3%82%92%E5%BC%95%E3%81%8D%E3%81%BE%E3%81%97%E3%81%9F"],
        ["冬院試に突入します",r"insi_img/school_samui_seifuku.png","%E9%99%A2%E8%A9%A6%E3%82%AC%E3%83%81%E3%83%A3%E3%81%A7%E3%83%8F%E3%82%BA%E3%83%AC%3A%E3%80%8C%E5%86%AC%E9%99%A2%E8%A9%A6%E3%81%AB%E7%AA%81%E5%85%A5%E3%81%97%E3%81%BE%E3%81%99%E3%80%8D%E3%82%92%E5%BC%95%E3%81%8D%E3%81%BE%E3%81%97%E3%81%9F"]
    ],
    #大ハズレ枠
    [
        ["書類選考で落ちます",r"insi_img/document_shinsa_fugoukaku.png","%E9%99%A2%E8%A9%A6%E3%82%AC%E3%83%81%E3%83%A3%E3%81%A7%E5%A4%A7%E3%83%8F%E3%82%BA%E3%83%AC%3A%E3%80%8C%E6%9B%B8%E9%A1%9E%E9%81%B8%E8%80%83%E3%81%A7%E8%90%BD%E3%81%A1%E3%81%BE%E3%81%99%E3%80%8D%E3%82%92%E5%BC%95%E3%81%8D%E3%81%BE%E3%81%97%E3%81%9F"],
        ["TOEFLで足切りされます",r"insi_img/document_shinsa_fugoukaku.png","%E9%99%A2%E8%A9%A6%E3%82%AC%E3%83%81%E3%83%A3%E3%81%A7%E5%A4%A7%E3%83%8F%E3%82%BA%E3%83%AC%3A%E3%80%8CTOEFL%E3%81%A7%E8%B6%B3%E5%88%87%E3%82%8A%E3%81%95%E3%82%8C%E3%81%BE%E3%81%99%E3%80%8D%E3%82%92%E5%BC%95%E3%81%8D%E3%81%BE%E3%81%97%E3%81%9F"],
        ["学部の成績不良で足切りされます",r"insi_img/document_shinsa_fugoukaku.png","%E9%99%A2%E8%A9%A6%E3%82%AC%E3%83%81%E3%83%A3%E3%81%A7%E5%A4%A7%E3%83%8F%E3%82%BA%E3%83%AC%3A%E3%80%8C%E5%AD%A6%E9%83%A8%E3%81%AE%E6%88%90%E7%B8%BE%E4%B8%8D%E8%89%AF%E3%81%A7%E8%B6%B3%E5%88%87%E3%82%8A%E3%81%95%E3%82%8C%E3%81%BE%E3%81%99%E3%80%8D%E3%82%92%E5%BC%95%E3%81%8D%E3%81%BE%E3%81%97%E3%81%9F"],
        ["カンニングと間違われて不合格になります",r"insi_img/cunning_cheating.png","%E9%99%A2%E8%A9%A6%E3%82%AC%E3%83%81%E3%83%A3%E3%81%A7%E5%A4%A7%E3%83%8F%E3%82%BA%E3%83%AC%3A%E3%80%8C%E3%82%AB%E3%83%B3%E3%83%8B%E3%83%B3%E3%82%B0%E3%81%A8%E9%96%93%E9%81%95%E3%82%8F%E3%82%8C%E3%81%A6%E4%B8%8D%E5%90%88%E6%A0%BC%E3%81%AB%E3%81%AA%E3%82%8A%E3%81%BE%E3%81%99%E3%80%8D%E3%82%92%E5%BC%95%E3%81%8D%E3%81%BE%E3%81%97%E3%81%9F"],
        ["共通数学で爆死して不合格です",r"insi_img/test0.png","%E9%99%A2%E8%A9%A6%E3%82%AC%E3%83%81%E3%83%A3%E3%81%A7%E5%A4%A7%E3%83%8F%E3%82%BA%E3%83%AC%3A%E3%80%8C%E5%85%B1%E9%80%9A%E6%95%B0%E5%AD%A6%E3%81%A7%E7%88%86%E6%AD%BB%E3%81%97%E3%81%A6%E4%B8%8D%E5%90%88%E6%A0%BC%E3%81%A7%E3%81%99%E3%80%8D%E3%82%92%E5%BC%95%E3%81%8D%E3%81%BE%E3%81%97%E3%81%9F"],
        ["専門科目レポートが書けず不合格です",r"insi_img/shimekiri_report_hakui_man.png","%E9%99%A2%E8%A9%A6%E3%82%AC%E3%83%81%E3%83%A3%E3%81%A7%E5%A4%A7%E3%83%8F%E3%82%BA%E3%83%AC%3A%E3%80%8C%E5%B0%82%E9%96%80%E7%A7%91%E7%9B%AE%E3%83%AC%E3%83%9D%E3%83%BC%E3%83%88%E3%81%8C%E6%9B%B8%E3%81%91%E3%81%9A%E4%B8%8D%E5%90%88%E6%A0%BC%E3%81%A7%E3%81%99%E3%80%8D%E3%82%92%E5%BC%95%E3%81%8D%E3%81%BE%E3%81%97%E3%81%9F"],
        ["専門科目レポートの出し忘れで不合格です",r"insi_img/document_report.png","%E9%99%A2%E8%A9%A6%E3%82%AC%E3%83%81%E3%83%A3%E3%81%A7%E5%A4%A7%E3%83%8F%E3%82%BA%E3%83%AC%3A%E3%80%8C%E5%B0%82%E9%96%80%E7%A7%91%E7%9B%AE%E3%83%AC%E3%83%9D%E3%83%BC%E3%83%88%E3%81%AE%E5%87%BA%E3%81%97%E5%BF%98%E3%82%8C%E3%81%A7%E4%B8%8D%E5%90%88%E6%A0%BC%E3%81%A7%E3%81%99%E3%80%8D%E3%82%92%E5%BC%95%E3%81%8D%E3%81%BE%E3%81%97%E3%81%9F"],
        ["試験本番で解答用紙に名前を書き忘れて不合格です",r"insi_img/test0.png","%E9%99%A2%E8%A9%A6%E3%82%AC%E3%83%81%E3%83%A3%E3%81%A7%E5%A4%A7%E3%83%8F%E3%82%BA%E3%83%AC%3A%E3%80%8C%E8%A9%A6%E9%A8%93%E6%9C%AC%E7%95%AA%E3%81%A7%E8%A7%A3%E7%AD%94%E7%94%A8%E7%B4%99%E3%81%AB%E5%90%8D%E5%89%8D%E3%82%92%E6%9B%B8%E3%81%8D%E5%BF%98%E3%82%8C%E3%81%A6%E4%B8%8D%E5%90%88%E6%A0%BC%E3%81%A7%E3%81%99%E3%80%8D%E3%82%92%E5%BC%95%E3%81%8D%E3%81%BE%E3%81%97%E3%81%9F"],
        ["合格するも入学金を払い忘れて合格を取り消されます",r"insi_img/money_tokeru_yen.png","%E9%99%A2%E8%A9%A6%E3%82%AC%E3%83%81%E3%83%A3%E3%81%A7%E5%A4%A7%E3%83%8F%E3%82%BA%E3%83%AC%3A%E3%80%8C%E5%90%88%E6%A0%BC%E3%81%99%E3%82%8B%E3%82%82%E5%85%A5%E5%AD%A6%E9%87%91%E3%82%92%E6%89%95%E3%81%84%E5%BF%98%E3%82%8C%E3%81%A6%E5%90%88%E6%A0%BC%E3%82%92%E5%8F%96%E3%82%8A%E6%B6%88%E3%81%95%E3%82%8C%E3%81%BE%E3%81%99%E3%80%8D%E3%82%92%E5%BC%95%E3%81%8D%E3%81%BE%E3%81%97%E3%81%9F"],
        ["出願書類の不備で落とされます",r"insi_img/document_shinsa_fugoukaku.png","%E9%99%A2%E8%A9%A6%E3%82%AC%E3%83%81%E3%83%A3%E3%81%A7%E5%A4%A7%E3%83%8F%E3%82%BA%E3%83%AC%3A%E3%80%8C%E5%87%BA%E9%A1%98%E6%9B%B8%E9%A1%9E%E3%81%AE%E4%B8%8D%E5%82%99%E3%81%A7%E8%90%BD%E3%81%A8%E3%81%95%E3%82%8C%E3%81%BE%E3%81%99%E3%80%8D%E3%82%92%E5%BC%95%E3%81%8D%E3%81%BE%E3%81%97%E3%81%9F"],
        ["合格するも4Aの演習を落として留年します",r"insi_img/school_tani_otosu_girl.png","%E9%99%A2%E8%A9%A6%E3%82%AC%E3%83%81%E3%83%A3%E3%81%A7%E5%A4%A7%E3%83%8F%E3%82%BA%E3%83%AC%3A%E3%80%8C%E5%90%88%E6%A0%BC%E3%81%99%E3%82%8B%E3%82%824A%E3%81%AE%E6%BC%94%E7%BF%92%E3%82%92%E8%90%BD%E3%81%A8%E3%81%97%E3%81%A6%E7%95%99%E5%B9%B4%E3%81%97%E3%81%BE%E3%81%99%E3%80%8D%E3%82%92%E5%BC%95%E3%81%8D%E3%81%BE%E3%81%97%E3%81%9F"],
        ["合格するも卒論が書けず留年します",r"insi_img/school_ryunen.png","%E9%99%A2%E8%A9%A6%E3%82%AC%E3%83%81%E3%83%A3%E3%81%A7%E5%A4%A7%E3%83%8F%E3%82%BA%E3%83%AC%3A%E3%80%8C%E5%90%88%E6%A0%BC%E3%81%99%E3%82%8B%E3%82%82%E5%8D%92%E8%AB%96%E3%81%8C%E6%9B%B8%E3%81%91%E3%81%9A%E7%95%99%E5%B9%B4%E3%81%97%E3%81%BE%E3%81%99%E3%80%8D%E3%82%92%E5%BC%95%E3%81%8D%E3%81%BE%E3%81%97%E3%81%9F"],
        ["試験当日にコロナを発症して受験できません",r"insi_img/virus_corona.png","%E9%99%A2%E8%A9%A6%E3%82%AC%E3%83%81%E3%83%A3%E3%81%A7%E5%A4%A7%E3%83%8F%E3%82%BA%E3%83%AC%3A%E3%80%8C%E8%A9%A6%E9%A8%93%E5%BD%93%E6%97%A5%E3%81%AB%E3%82%B3%E3%83%AD%E3%83%8A%E3%82%92%E7%99%BA%E7%97%87%E3%81%97%E3%81%A6%E5%8F%97%E9%A8%93%E3%81%A7%E3%81%8D%E3%81%BE%E3%81%9B%E3%82%93%E3%80%8D%E3%82%92%E5%BC%95%E3%81%8D%E3%81%BE%E3%81%97%E3%81%9F"],
        ["夏院試にも冬院試にも落ちます",r"insi_img/fugoukaku.png","%E9%99%A2%E8%A9%A6%E3%82%AC%E3%83%81%E3%83%A3%E3%81%A7%E5%A4%A7%E3%83%8F%E3%82%BA%E3%83%AC%3A%E3%80%8C%E5%A4%8F%E9%99%A2%E8%A9%A6%E3%81%AB%E3%82%82%E5%86%AC%E9%99%A2%E8%A9%A6%E3%81%AB%E3%82%82%E8%90%BD%E3%81%A1%E3%81%BE%E3%81%99%E3%80%8D%E3%82%92%E5%BC%95%E3%81%8D%E3%81%BE%E3%81%97%E3%81%9F"],
        ["冬院試に突入して卒論が書ききれず留年します",r"insi_img/school_ryunen.png","%E9%99%A2%E8%A9%A6%E3%82%AC%E3%83%81%E3%83%A3%E3%81%A7%E5%A4%A7%E3%83%8F%E3%82%BA%E3%83%AC%3A%E3%80%8C%E5%86%AC%E9%99%A2%E8%A9%A6%E3%81%AB%E7%AA%81%E5%85%A5%E3%81%97%E3%81%A6%E5%8D%92%E8%AB%96%E3%81%8C%E6%9B%B8%E3%81%8D%E3%81%8D%E3%82%8C%E3%81%9A%E7%95%99%E5%B9%B4%E3%81%97%E3%81%BE%E3%81%99%E3%80%8D%E3%82%92%E5%BC%95%E3%81%8D%E3%81%BE%E3%81%97%E3%81%9F"]
    ],
    #当たり枠
    [
        ["第一志望の研究室に合格します",r"insi_img/medal1.png","%E9%99%A2%E8%A9%A6%E3%82%AC%E3%83%81%E3%83%A3%E3%81%A7%E5%BD%93%E3%81%9F%E3%82%8A%3A%E3%80%8C%E7%AC%AC%E4%B8%80%E5%BF%97%E6%9C%9B%E3%81%AE%E7%A0%94%E7%A9%B6%E5%AE%A4%E3%81%AB%E5%90%88%E6%A0%BC%E3%81%97%E3%81%BE%E3%81%99%E3%80%8D%E3%82%92%E5%BC%95%E3%81%8D%E3%81%BE%E3%81%97%E3%81%9F"],
        ["第二志望の研究室に合格します",r"insi_img/medal2.png","%E9%99%A2%E8%A9%A6%E3%82%AC%E3%83%81%E3%83%A3%E3%81%A7%E5%BD%93%E3%81%9F%E3%82%8A%3A%E3%80%8C%E7%AC%AC%E4%BA%8C%E5%BF%97%E6%9C%9B%E3%81%AE%E7%A0%94%E7%A9%B6%E5%AE%A4%E3%81%AB%E5%90%88%E6%A0%BC%E3%81%97%E3%81%BE%E3%81%99%E3%80%8D%E3%82%92%E5%BC%95%E3%81%8D%E3%81%BE%E3%81%97%E3%81%9F"],
        ["第三志望の研究室に合格します",r"insi_img/medal3.png","%E9%99%A2%E8%A9%A6%E3%82%AC%E3%83%81%E3%83%A3%E3%81%A7%E5%BD%93%E3%81%9F%E3%82%8A%3A%E3%80%8C%E7%AC%AC%E4%B8%89%E5%BF%97%E6%9C%9B%E3%81%AE%E7%A0%94%E7%A9%B6%E5%AE%A4%E3%81%AB%E5%90%88%E6%A0%BC%E3%81%97%E3%81%BE%E3%81%99%E3%80%8D%E3%82%92%E5%BC%95%E3%81%8D%E3%81%BE%E3%81%97%E3%81%9F"],
        ["共通数学で全完します",r"insi_img/100ten.png","%E9%99%A2%E8%A9%A6%E3%82%AC%E3%83%81%E3%83%A3%E3%81%A7%E5%BD%93%E3%81%9F%E3%82%8A%3A%E3%80%8C%E5%85%B1%E9%80%9A%E6%95%B0%E5%AD%A6%E3%81%A7%E5%85%A8%E5%AE%8C%E3%81%97%E3%81%BE%E3%81%99%E3%80%8D%E3%82%92%E5%BC%95%E3%81%8D%E3%81%BE%E3%81%97%E3%81%9F"],
        ["院試レポートで満点がもらえます",r"insi_img/100ten.png","%E9%99%A2%E8%A9%A6%E3%82%AC%E3%83%81%E3%83%A3%E3%81%A7%E5%BD%93%E3%81%9F%E3%82%8A%3A%E3%80%8C%E9%99%A2%E8%A9%A6%E3%83%AC%E3%83%9D%E3%83%BC%E3%83%88%E3%81%A7%E6%BA%80%E7%82%B9%E3%81%8C%E3%82%82%E3%82%89%E3%81%88%E3%81%BE%E3%81%99%E3%80%8D%E3%82%92%E5%BC%95%E3%81%8D%E3%81%BE%E3%81%97%E3%81%9F"],
        ["併願で受かります",r"insi_img/juken_goukaku_daruma.png","%E9%99%A2%E8%A9%A6%E3%82%AC%E3%83%81%E3%83%A3%E3%81%A7%E5%BD%93%E3%81%9F%E3%82%8A%3A%E3%80%8C%E4%BD%B5%E9%A1%98%E3%81%A7%E5%8F%97%E3%81%8B%E3%82%8A%E3%81%BE%E3%81%99%E3%80%8D%E3%82%92%E5%BC%95%E3%81%8D%E3%81%BE%E3%81%97%E3%81%9F"],
        ["口述試験で満点をとります",r"insi_img/100ten.png","%E9%99%A2%E8%A9%A6%E3%82%AC%E3%83%81%E3%83%A3%E3%81%A7%E5%BD%93%E3%81%9F%E3%82%8A%3A%E3%80%8C%E5%8F%A3%E8%BF%B0%E8%A9%A6%E9%A8%93%E3%81%A7%E6%BA%80%E7%82%B9%E3%82%92%E3%81%A8%E3%82%8A%E3%81%BE%E3%81%99%E3%80%8D%E3%82%92%E5%BC%95%E3%81%8D%E3%81%BE%E3%81%97%E3%81%9F"],
        ["夏院試に落ちるも冬院試で合格します",r"insi_img/juken_goukakuhappyou_happy.png","%E9%99%A2%E8%A9%A6%E3%82%AC%E3%83%81%E3%83%A3%E3%81%A7%E5%BD%93%E3%81%9F%E3%82%8A%3A%E3%80%8C%E5%A4%8F%E9%99%A2%E8%A9%A6%E3%81%AB%E8%90%BD%E3%81%A1%E3%82%8B%E3%82%82%E5%86%AC%E9%99%A2%E8%A9%A6%E3%81%A7%E5%90%88%E6%A0%BC%E3%81%97%E3%81%BE%E3%81%99%E3%80%8D%E3%82%92%E5%BC%95%E3%81%8D%E3%81%BE%E3%81%97%E3%81%9F"]
    ]
]

"""for i in gacha_list[2]:
    print(i[0],urllib.parse.unquote(i[1].replace("%3A","")))"""

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

    """if rarity_index==0:
        rarity="ハズレ"
        background_color="#a9a9a9"
        sentence_color="#000000"
    elif rarity_index==1:
        rarity="大ハズレ"
        background_color="#000000"
        sentence_color="#ff0000"
    else:
        rarity="あたり"
        background_color="ffd700"
        sentence_color="#000000"""
    
    if rarity_index==0:
        rarity="ハズレ"
        background_color="DarkGrey"
        sentence_color="#000000"
    elif rarity_index==1:
        rarity="大ハズレ"
        background_color="Black"
        sentence_color="#ff0000"
    else:
        rarity="あたり"
        background_color="LightYellow"
        sentence_color="#000000"
       
    return result_tweet,background_color,[[sg.Image(result_image)],[sg.Text(rarity+result_sentence,text_color=sentence_color)]]
#print(insi_gacha())
