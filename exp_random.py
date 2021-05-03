import tkinter as tk
from tkinter import messagebox
import random

def scrape_weather():
  import requests
  from bs4 import BeautifulSoup

  #tenki.jpの目的の地域のページのURL(東京都文京区)
  url = 'https://tenki.jp/forecast/3/16/4410/13105/'

  #HTTPリクエスト
  r = requests.get(url)

  bsObj = BeautifulSoup(r.content, "html.parser")

  #今日の天気を取得
  today = bsObj.find(class_="today-weather")
  weather = today.p.string

  #気温情報のまとまり
  temp=today.div.find(class_="date-value-wrap")

  #気温の取得
  temp=temp.find_all("dd")
  temp_max = int(temp[0].span.string) #最高気温
  temp_min = int(temp[2].span.string) #最低気温

  return([temp_max, temp_min])

# click時のイベント
def btn_click():
  x = random.random()
  w = scrape_weather()
  y = w[0]
  z = w[1]
  lucky = x * (y + z)
  messagebox.showinfo("今日の乱数",lucky)

# 画面作成
tki = tk.Tk()
tki.geometry('300x200') # 画面サイズの設定
tki.title('ボタンのサンプル') # 画面タイトルの設定

# ボタンの作成
btn = tk.Button(tki, text='ボタン', command = btn_click)
btn.place(x=130, y=80) #ボタンを配置する位置の設定

# 画面をそのまま表示
tki.mainloop()