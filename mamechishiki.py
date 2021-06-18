### 使い方
### import mamechishiki
### layout.append(mamechishiki.get_mamechishiki_list())
### すればとりあえず動く。3 行分を使って、「今日の豆知識！」「本文」「ソース」を出す。
###
### さらに次の追加を行うことで、「ソースをクリックするとページを開く機能」を追加できる。
### (i) import webbrowser を追加。
### (ii) 次の ... 以降の条件分岐を追加する。
###     while True:
###         event, values = windows.read()
###         ...
###         # key = "URL (具体的なurl)" である sg.Text がクリックされたらリンク先を開く
###         if event.startswith("URL "):
###             url = event.split(' ')[1]
###             webbrowser.open(url)
### 
### 参考：https://stackoverflow.com/questions/66866390/in-pysimplegui-how-can-i-have-a-hyperlink-in-a-text-field
### リンク機能についての補足：
### ・他に sg.Text からリンクっぽいことをしたい人がいた場合、仕様を統一した方がいいかも
### ・紛らわしいのでメモしておくと、青字+下線はフォントとしてつけてるだけで、自動でハイパーリンク化する機能があるわけではない。
### ・単純に、「key = "URL (具体的なurl)" を指定してある sg.Text をクリックする」と、「(具体的なurl) を開くイベントを発生させる」だけである。
### ・リアルタイムでアプリに反応してもらわないといけないため、多分 main.py での while 文の書き換えは必要

import PySimpleGUI as sg
import random

#豆知識のメインとなる文
mamechishiki_list = [
    # 0 ~ 5 : 確率分布についての豆知識
    "23人の人がいると、50%以上の確率で同じ誕生日の組がいる。",
    "指数分布と幾何分布は、Pr(X>t+s | X>t) = Pr(X>s)で表される\n「無記憶性」を持つ。",
    "ランダムなイベントに対し、指数分布は発生間隔、\nポアソン分布は単位時間での発生回数を表す。",
    "小規模かつランダムなあみだくじは偏りがある。\n縦線6本・横線10本（完全ランダム）の場合、\n左端→左端：37.4%に対し、左端→右端：1.3%しかない。",
    "n種類のコンプガチャを2nlogn回(=期待回数の2倍)\n引いた場合、コンプリート出来ない確率は1/n以下。",
    "多人数でのじゃんけんはオススメしない。\n10人だと、1回当たりのあいこの確率が94.8%となる。",
    # 6 ~ 7 : 降水確率についての豆知識
    "降水確率の予報と実際の結果を比較すると、\n予報が50%以下だった場合の実際の降水確率は、予報よりおよそ10%低い。",
    "気象庁は毎日夕方に「明日の降水の有無」の予報を出している。\n的中率は徐々に上がり、東京地方では現在85%超である。"
]

#豆知識のメインとなる文(tweet用)
mamechishiki_list_for_tweet = [
    # 0 ~ 5 : 確率分布についての豆知識
    "23人の人がいると、50%以上の確率で同じ誕生日の組がいる。",
    "指数分布と幾何分布は、Pr(X>t+s|X>t)=Pr(X>s)で表される「無記憶性」を持つ。",
    "ランダムなイベントに対し、指数分布は発生間隔、ポアソン分布は単位時間での発生回数を表す。",
    "小規模かつランダムなあみだくじは偏りがある。縦線6本・横線10本（完全ランダム）の場合、左端→左端：37.4%25に対し、左端→右端：1.3%25しかない。",
    "n種類のコンプガチャを2nlogn回(=期待回数の2倍)引いた場合、コンプリート出来ない確率は1/n以下。",
    "多人数でのじゃんけんはオススメしない。10人だと、1回当たりのあいこの確率が94.8%25となる。",
    # 6 ~ 7 : 降水確率についての豆知識
    "降水確率の予報と実際の結果を比較すると、予報が50%25以下だった場合の実際の降水確率は、予報よりおよそ10%25低い。",
    "気象庁は毎日夕方に「明日の降水の有無」の予報を出している。的中率は徐々に上がり、東京地方では現在85%25超である。"
]

#[豆知識の参考記事のタイトル, URL]
mamechishiki_source = [
    # 0 ~ 5 : 確率分布についての豆知識
    ["同じ誕生日の二人組がいる確率について（高校数学の美しい物語）", "https://manabitimes.jp/math/996"],
    ["Memorylessness（Wikipedia）", "https://en.wikipedia.org/wiki/Memorylessness"],
    ["指数分布の意味と具体例（高校数学の美しい物語）", "https://manabitimes.jp/math/1006"],
    ["あみだくじの確率を計算してみた（高校数学の美しい物語）", "https://manabitimes.jp/math/1157"],
    ["ブールの不等式の証明と応用例（高校数学の美しい物語）", "https://manabitimes.jp/math/1252"],
    ["じゃんけんであいこになる確率の求め方と値（高校数学の美しい物語）", "https://manabitimes.jp/math/1172"],
    # 6 ~ 7 : 降水確率についての豆知識
    ["天気予報検証結果（気象庁）", "https://www.data.jma.go.jp/fcd/yoho/data/kensho/score_f.html"],
    ["天気予報の精度検証結果（気象庁）", "https://www.data.jma.go.jp/fcd/yoho/kensho/yohohyoka_top.html"]
]

mamechishiki_img = [
    r"background_img/small_same_birthday.png"
]

# random.randint を用いて [豆知識の文, [ソース記事タイトル, ソース記事url]] を返す
def mame_set():
    sz = min(len(mamechishiki_list), len(mamechishiki_source))
    random_index = random.randint(0, sz - 1)
    return mamechishiki_list_for_tweet[random_index], mamechishiki_list[random_index], mamechishiki_source[random_index], mamechishiki_img[0]

# layout に挿入できる形式でのリストを返す
def get_mamechishiki_list():
    tweet, sentence, source, img_path = mame_set()
    tweet += "%0D%0A出典：" + source[0] + ",%20" + source[1]
    my_list = [
            [sg.Text("今日の豆知識！", font = ('Yu Gothic', 12), text_color = "#ffff33")], 
            [sg.Text(sentence, font = ('Yu Gothic', 11))], 
            [sg.Text("詳しくは→ ", font = ('Yu Gothic', 11)),
             sg.Text(source[0], tooltip = source[1], enable_events = True, font = ('Yu Gothic', 11, "underline"), text_color = "#0000ff", key = f'URL {source[1]}')]
    ]
    # return tweet, img_path, my_list
    return my_list

