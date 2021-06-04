#明日の予想天気、最高気温、最低気温、降水確率をリストで出力する関数

#ライブラリのインポート
import requests
from bs4 import BeautifulSoup
  
def return_weather():

  #tenki.jpの目的の地域のページのURL（暫定で東京都文京区)
  url='https://tenki.jp/forecast/3/16/4410/13105/'
  #HTTPリクエスト
  r = requests.get(url)

  #HTMLの解析
  bsObj = BeautifulSoup(r.content, "html.parser")

  #明日の天気を取得
  tomorrow = bsObj.find(class_="tomorrow-weather")
  weather = tomorrow.p.string

  #気温情報のまとまり
  temp=tomorrow.div.find(class_="date-value-wrap")

  #気温の取得
  temp=temp.find_all("dd")
  temp_max = temp[0].span.string #最高気温
  temp_min = temp[2].span.string #最低気温

  #降水確率情報のまとまり
  precip=tomorrow.find(class_="rain-probability")
  precip_strip=precip.find_all("td")

  #降水確率情報の取得
  precip_array=[]
  for item in precip_strip:
    val=int(item.select_one(".unit").previous_sibling)
    precip_array.append(val)
    
  #天気予報に画像を対応させる
  weather_image=None
  weather_image_list=[r'img\sunny_man.png', r'img\cloudy_image.png', r'img\rain_man.png']
  if '晴' in weather:
    weather_image=weather_image_list[0]
  elif '雨' in weather:
    weather_image=weather_image_list[2]
  elif '曇' in wetather:
    weather_image=weather_image_list[1]

  #結果の出力
  weather_prediction=[weather, temp_max, temp_min, precip_array]
  return [map(sg.Image, weather_image),map(sg.Text, weather_prediction)]
