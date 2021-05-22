import tkinter as tk
import random

# ボタンを押したときの処理 --- (*1)
def hukou():
    s = random.random()
    if s < 0.2:
        result = "交通事故"
    elif s < 0.6:
        result = "雷直撃"
    elif s < 0.8:
        result = "飛行機墜落"
    else:
        result = "平和な一日"
    # 結果をラベルに表示
    labelResult['text'] = result

# ウィンドウを作成 --- (*2)
win = tk.Tk()
win.title("不幸ガチャ")
win.geometry("250x100")

# 部品を作成 --- (*3)
labelResult = tk.Label(win, text=u'今日のあなたは')
labelResult.pack()

calcButton = tk.Button(win, text=u'占う')
calcButton["command"] = hukou
calcButton.pack()

# ウィンドウを動かす
win.mainloop()