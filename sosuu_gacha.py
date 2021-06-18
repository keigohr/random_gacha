import PySimpleGUI as sg
import random

judge_num = 10

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

# input n : odd, > 100
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
    n = random.randint(50, 10**30) * 2 + 1
    tweet = res = f"{n}は"
    prime = miller_rabin_primality_test(n)
    if prime:
        probability = 1<<(judge_num * 2)
        probability = (probability - 1) * 100.0 / probability
        #res += f"prime. (more than {probability}%)"
        tweet += f"{probability:.6f}%25以上の確率で素数です！"
        res += f"{probability:.6f}%以上の確率で素数です！"
        print(res)
    else:
        res += "合成数です。"
        tweet += "合成数です。"
    return tweet, prime, res

def sosuu_gacha():
    prime, sentence = miller_rabin_output()
    if prime:
        return tweet, "BluePurple", [[sg.Text(sentence)]]
    else:
        return tweet, "Purple", [[sg.Text(sentence)]]

### for _ in range(1000):
###    miller_rabin_output()
