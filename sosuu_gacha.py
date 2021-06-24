import PySimpleGUI as sg
import random

judge_num = 10
gacha_num = 15 ###gacha_num = 0 mod 5

def fast_pow(_n, pw, mod):
    res = 1
    dbl = _n
    while pw > 0:
        if pw&1:
            res *= dbl
            res %= mod
        dbl *= dbl
        dbl %= mod
        pw >>= 1
    return res

### input n : odd, > 100
def miller_rabin_primality_test(n):
    s = 0
    d = n - 1
    while (d&1) == 0:
        s += 1
        d >>= 1
    for _ in range(judge_num):
        a = random.randint(1, n - 1)
        composite = fast_pow(a, d, n) != 1
        for r in range(s):
            composite = composite and fast_pow(a, d<<r, n) != n - 1
        if composite:
            return False
    return True

def miller_rabin_output():
    n = random.randint(51, 5 * (10**29)) * 2 - 1
    prime = miller_rabin_primality_test(n)
    return prime, n

def n_to_image(n, texttheme):
    n_copy = n
    res = []
    while n_copy > 0:
        res.append(sg.Image('./sosuu_img/sby' + str(n_copy%10) + '.png', background_color = texttheme, pad=((0, 0), (0, 0))))
        n_copy //= 10
    res.reverse()
    return res

def n_to_str30(n):
    temp_n = str(n)
    s = ""
    for _ in range(30 - len(temp_n)):
        s += "  "
    s += temp_n
    return s

def sosuu_gacha():
    res_of_composite = []
    res_of_prime = []
    for _ in range(gacha_num):
        prime, number = miller_rabin_output()
        if prime:
            res_of_prime.append(number)
        else:
            res_of_composite.append(number)

    myfont = '游ゴシック'
    if len(res_of_prime) > 0:
        texttheme = mytheme = "DarkRed"
        mytextcolor = "yellow"
    else:
        texttheme = "#e3f2fd"
        mytheme = "LightBlue"
        mytextcolor = "black"

    layout = [[sg.Text(f"素数ガチャを{gacha_num}回引きました！", font = (myfont, 20), text_color = mytextcolor, background_color = texttheme)]]
    tweet = "素数ガチャを引きました%EF%BC%81%0D%0A"

    if len(res_of_prime) > 0:
        layout.append([sg.Text("おめでとうございます！", font = (myfont, 20), text_color = mytextcolor, background_color = texttheme)])
        for i, n in enumerate(res_of_prime):
            layout.append(n_to_image(n, texttheme))
            if i > 0:
                tweet += "%2C+"
            tweet += str(n)
        probability = 100.0 * (1.0 - pow(0.25, judge_num))
        layout.append([sg.Text(f"は{probability:.4f}%以上の確率で素数です！", font = (myfont, 20), text_color = mytextcolor, background_color = texttheme)])
        tweet += f"は{probability:.4f}%25以上の確率で素数です%EF%BC%81"
    else:
        layout.append([sg.Text("合成数しか出ませんでした......", font = (myfont, 30), text_color = mytextcolor, background_color = texttheme)])
        tweet += "合成数しか出ませんでした......"

    layout.append([sg.Text("引いた数", font = (myfont, 20), text_color = mytextcolor, background_color = texttheme)])
    temp_Text = []
    myfontsize = 75 // max(5, gacha_num // 2)
    for n in res_of_prime:
        temp_Text.append(sg.Text(n_to_str30(n), font = (myfont, myfontsize), text_color = mytextcolor, background_color = texttheme))
    if len(res_of_prime) > 0:
        mytextcolor = "white"
    for n in res_of_composite:
        temp_Text.append(sg.Text(n_to_str30(n), font = (myfont, myfontsize), text_color = mytextcolor, background_color = texttheme))
    
    yokohaba = max(1, gacha_num // 5)
    for i in range(gacha_num // yokohaba):
        one_line = [temp_Text[i * yokohaba]]
        for j in range(yokohaba - 1):
            one_line.append(sg.Text("     ", font = (myfont, myfontsize), text_color = mytextcolor, background_color = texttheme))
            one_line.append(temp_Text[i * yokohaba + 1 + j])
        layout.append(one_line)

    layout_with_column = [[sg.Column(layout, element_justification = 'center', background_color = texttheme)]]
    if prime:
        return tweet, mytheme, layout_with_column
    else:
        return tweet, mytheme, layout_with_column
