import tkinter as tk
from tkinter import ttk
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

def calc():
    
    #h = float(textHeight.get()) / 100
    # 結果をラベルに表示
    s = comboDistribution.get()
    average = float(textAverage.get())
    scatter = float(textScatter.get())
    if s == "normal":
        result = np.random.normal(loc=average, scale=scatter)
    labelResult['text'] = result

# ウィンドウを作成
win = tk.Tk()
win.title("乱数生成")
win.geometry("500x250")


labelDistribution = tk.Label(win, text=u'分布')
labelDistribution.pack()

dis = ["normal"]
variable = "distribution"
comboDistribution = ttk.Combobox(values=dis,textvariable=variable)
comboDistribution.pack()

labelAverage = tk.Label(win, text=u'平均')
labelAverage.pack()

textAverage = tk.Entry(win)
textAverage.insert(tk.END, '0')
textAverage.pack()

labelScatter = tk.Label(win, text=u'分散')
labelScatter.pack()

textScatter = tk.Entry(win)
textScatter.insert(tk.END, '1')
textScatter.pack()


labelResult = tk.Label(win, text=u'---')
labelResult.pack()

calcButton = tk.Button(win, text=u'計算')
calcButton["command"] = calc
calcButton.pack()

# ウィンドウを動かす
win.mainloop()