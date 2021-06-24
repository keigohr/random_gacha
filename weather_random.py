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

  '''
  #10日間天気のまとまり
  precip=bsObj.find(class_="forecast-point-week")

  #10日間降水確率の取得
  precip_strip=precip.find_all(class_="precip")
  precip_array=[]
  for item in precip_strip:
    val=int(item.select_one(".precip .unit").previous_sibling)
    precip_array.append(val)
  '''
    
  #降水確率情報のまとまり
  tomorrow = bsObj.find(class_="tomorrow-weather")
  precip=tomorrow.find(class_="rain-probability")
  precip_strip=precip.find_all("td")

  #降水確率情報の取得
  precip_array=[]
  for item in precip_strip:
    val=int(item.select_one(".unit").previous_sibling)
    precip_array.append(val)

  return(precip_array)

def generate_probability():
  #probability=sum(scrape_weather())/len(scrape_weather())
  probability=scrape_weather()[2]
  return int(probability)
  
def return_weather():
  
  #天気予報をランダムに生成する、天気予報に画像を対応させる
  weather_image=None
  weather_list=[]
  weathers1=[]
  weathers2=[]
  background_color=None
  weather_list=['晴れ', '雨' ]
  weather_image_list=[r'img\sunny_man.png', r'img\rain_man.png']
  #background_color_list=['LightGreen4', 'Reddit'] 

  rain_number=0
  
  value = generate_probability()
  index_choice=[0, 1]
  index_list = random.choices(index_choice, weights=(100-value, value), k=5)
  for index in index_list:
    weather_image=weather_image_list[index]
    weathers1.append(sg.Image(weather_image, background_color='yellow'))
    rain_number+=index

  index_list = random.choices(index_choice, weights=(100-value, value), k=5)
  for index in index_list:
    weather_image=weather_image_list[index]
    weathers2.append(sg.Image(weather_image, background_color='yellow'))
    rain_number+=index

  background_color='LightGreen4'
    
  #ツイートする文面を生成
  #tweet="降水確率:{0}%25%0A天気:{1}".format(value, weather)
  tweet="降水確率:{0}%25".format(value)
  #content="降水確率:{0}%\n天気:{1}".format(value, weather)
  
  content0="今日の天気"
  content1="降水確率は{0}%です。".format(value)
  content2="あなたは10回中{0}回雨にぬれました。".format(rain_number)
  
  #結果の出力
  #for weather in weather_list
  #test = [sg.Image(weather_list)]
  
  myfont = 'UD デジタル 教科書体 NP-R'
  layout_column=[[sg.Text(content0, font = (myfont, 20), background_color='yellow')], [sg.Text(content1,font = (myfont, 20), background_color='yellow')], weathers1, weathers2, [sg.Text(content2,font = (myfont, 20), background_color='yellow')]]
  layout = [[sg.Column(layout_column, element_justification='center', background_color='yellow')]]
  return content2, background_color, layout
