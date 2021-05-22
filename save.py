import tkinter as tk
from tkinter import filedialog
import configparser

# configparserのインスタンス化
config = configparser.ConfigParser()
# 読込むiniファイルを指定
config.read("./config.ini")

##### 関数  #####
# ファイルパスの取得
def get_path():
    # グローバル変数
    global file_path
    typ = [("Text","*.txt")]
    file_path = filedialog.askopenfilename(filetypes = typ)
    
# iniへファイルパスを保存
def path_save(): 
    config["Path"] = {"Text" : file_path}
    # iniファイルへ保存
    with open("config.ini", "w") as file:
        config.write(file)

#####  GUI  #####
root = tk.Tk()
root.geometry("300x100")

# ボタン
push_button = tk.Button(root, text = "Push", command = lambda:[get_path(), path_save()])
push_button.place(x = 30, y = 30)

root.mainloop()