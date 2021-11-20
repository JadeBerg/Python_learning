import math
import requests


def frequency(s):
    low = s.lower()
    I = 0
    dict_counter = {}
    for char in low:
        if not dict_counter or char not in dict_counter.keys():
            dict_counter.update({char: 1})
        elif char in dict_counter.keys():
            dict_counter[char] += 1
    for key, val in dict_counter.items():
        f = round(val / len(s), 4)
        if f != 0:
            I += f * math.log2(f)
    print("\nКоличество информации: ", round(-I * len(s), 2))


def get_text(u):
    rs = requests.get(u)
    return rs.text


url = str(input())
text = get_text(url)
frequency(text)
