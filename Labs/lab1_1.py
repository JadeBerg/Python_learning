import math


def frequency(s):
    low = s.lower()
    A = []
    I = 0
    dict_counter = {}
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
               "v", "w", "x", "y", "z", "а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о",
               "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я", "ґ", "є", "і", "ї"]
    for char in letters:
        dict_counter.update({char: 0})
    for char in low:
        if not dict_counter or char not in dict_counter.keys():
            dict_counter.update({char: 1})
        elif char in dict_counter.keys():
            dict_counter[char] += 1
    for key, val in dict_counter.items():
        f = round(val / len(s), 4)
        if f != 0:
            A.append(f)
            I += f * math.log2(f)
        print('Символ:', key, '', 'Встречается:', val, 'раз ', 'Частота появления:', f)
    print("\nОтсортированная частота: ", sorted(A))
    print("\nКоличество информации: ", round(-I * len(s), 2))


a = str(input())
frequency(a)
