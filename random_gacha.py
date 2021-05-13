﻿import sys
import json, config
from urllib import request
import tkinter as tk
from tkinter import messagebox
import random

from requests_oauthlib import OAuth1Session

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET
twitter = OAuth1Session(CK, CS, AT, ATS)

def scrape_weather():
  import requests
  from bs4 import BeautifulSoup

  #tenki.jpの目的の地域のページのURL(東京都文京区)
  url = 'https://tenki.jp/forecast/3/16/4410/13105/'

  #HTTPリクエスト
  r = requests.get(url)

  bsObj = BeautifulSoup(r.content, "html.parser")

  #10日間天気のまとまり
  precip=bsObj.find(class_="forecast-point-week")

  #10日間降水確率の取得
  precip_strip=precip.find_all(class_="precip")
  precip_array=[]
  for item in precip_strip:
    val=int(item.select_one(".precip .unit").previous_sibling)
    precip_array.append(val)

  return(precip_array)

def tweet():

       url = "https://api.twitter.com/1.1/statuses/update.json"        
       params = {"status":"今日の乱数は{}でした！".format(lucky)}


       req = twitter.post(url, params = params)

       if req.status_code == 200:
              print ("OK")
       else:
              print ("Error")

# click時のイベント
def btn_click():
  x = random.random()
  y = random.choice(scrape_weather())
  lucky = x * y
  ret = messagebox.showinfo("今日の乱数","今日の乱数は{}です。Twitterで共有しますか？".format(lucky))
  if ret == True:
    tweet()

# 画面作成
tki = tk.Tk()
tki.geometry('300x200') # 画面サイズの設定
tki.title('ボタンのサンプル') # 画面タイトルの設定

# ボタンの作成
btn1 = tk.Button(tki, text='ボタン', command = btn_click)
btn1.place(x=130, y=80) #ボタンを配置する位置の設定

# 画面をそのまま表示
tki.mainloop()