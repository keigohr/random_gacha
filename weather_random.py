#今日の降水確率と予想天気をリストで出力する関数

#ライブラリのインポート
import requests
from bs4 import BeautifulSoup
import PySimpleGUI as sg
import random

def scrape_weather():
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

def generate_probability():
  probability=sum(scrape_weather())/len(scrape_weather())
  return int(probability)
  
def return_weather():
  
  #天気予報をランダムに生成する、天気予報に画像を対応させる
  weather=None
  weather_image=None
  background_color=None
  weather_list=['晴れ', '曇り', '雨', '暴風雨', '雷雨' ]
  weather_image_list=[r'img\sunny_man.png', r'img\cloudy_image.png', r'img\rain_man.png', r'img\tenki_boufuu.png', r'img\thunder_girl.png']
  background_color_list=['LightGreen4', 'LightBlue7', 'Reddit', 'DarkTeal5', 'DarkBrown1'] 
  
  value = generate_probability()
  index = int(value/20)
  weather=weather_list[index]
  weather_image=weather_image_list[index]
  background_color=background_color_list[index]
    
  #ツイートする文面を生成
  tweet="降水確率：{0}%25 %0A 天気: {1}".format(value, weather)
  content="降水確率：{0}% \n 天気: {1}".format(value, weather)

  #背景画像の指定
  #background_image=r'background_img\weather.jpg'
  
  #結果の出力
  test = [sg.Image(weather_image)]
  test.append([sg.Text(content)])
  #return tweet, background_image, background_color, [test]
  return tweet, background_color, [test]
