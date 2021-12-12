from math import copysign, fabs, floor, isfinite, modf


def coding(word, alphabet, p):
    left, right = 0, 1
    for letter in word:
        i = alphabet.index(letter)
        left, right = (left + (right - left) * sum(p[:i]),
                       left + (right - left) * sum(p[: i + 1]))
        left = left/1.001
        right = right/1.0001
        print(letter, ":", left, "-", right)
    tag = (left + right) / 2.0
    print(tag)
    print(float_to_bin_fixed(tag))


def float_to_bin_fixed(f):
    if not isfinite(f):
        return repr(f)

    sign = '-' * (copysign(1.0, f) < 0)
    frac, fint = modf(fabs(f))
    n, d = frac.as_integer_ratio()
    assert d & (d - 1) == 0
    return f'{sign}{floor(fint):b}.{n:0{d.bit_length() - 1}b}'


def freq(alph, w):
    f = []
    for i in alph:
        if (i in w):
            f.append(w.count(i) / len(w))
        else:
            f.append(0)
    return f


alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ,.!-"—()?'
word = str(input())
p = freq(alphabet, word)
print(len(word))
coding(word, alphabet, p)
