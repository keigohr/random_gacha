import tkinter
import requests
import json

# 今日の天気を表示
def today_weather():
    update_weather(0)

# 明日の天気を表示
def yesterday_weather():
    # ラベルにメッセージを設定
    update_weather(1)

# 今日の天気を表示
def update_weather(date_num):
    # ラベルにメッセージを設定
    t = display_weather(date_num)
    label["text"] = t['dateLabel'] + 'の天気は「' + t['telop'] + '」です'
    label.update()

# 天気情報を取得する
def display_weather(date_num):
    # 天気のURL設定 city_numberには都市の番号を指定
    url = "https://weather.tsukumijima.net/api/forecast/city/130010"

    # URLを取得
    response = requests.get(url)
    # URL取得結果のチェック
    response.raise_for_status()
    # 天気データを読み込む
    return json.loads(response.text)['forecasts'][date_num]

# キャンバスの表示
root = tkinter.Tk()
# タイトルの設定
root.title("お天気GUI")
root.resizable(False, False)
# キャンバスのサイズ設定
canvas = tkinter.Canvas(root, width=600, height=600)
# キャンバスの表示
canvas.pack()

# 今日の天気を文字で表示する
label = tkinter.Label(root, text="ボタンをクリックしてください", font=("Times New Roman", 25), bg="white")
label.place(x=30, y=150)

# ボタンを表示する
button = tkinter.Button(root, text="今日の天気", font=("Times New Roman", 20), command=today_weather, fg="skyblue")
button2 = tkinter.Button(root, text="明日の天気", font=("Times New Roman", 20), command=yesterday_weather, fg="skyblue")
button.place(x=200, y=300)
button2.place(x=200, y=350)
root.mainloop()