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