#明日の予想天気、最高気温、最低気温、降水確率をリストで出力する関数

def return_weather():

  #ライブラリのインポート
  import requests
  from bs4 import BeautifulSoup

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

  #結果の出力
  weather_prediction=[weather, temp_max, temp_min, precip_array]
  return(weather_prediction)