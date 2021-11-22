import random
import numpy as np
import math as mt


def create_m(n):
    m = [[round(random.random() / n, 4) for i in range(n)] for j in range(n)]
    return m


def create_p_1(m):
    a = []
    e = 2.71828
    for i in range(m):
        p = pow(e, -1) / mt.factorial(i)
        a.append(p)
    return a


def create_p_2(m):
    e = 2.71828
    a = []
    for i in range(m):
        p = pow(2, i) * pow(e, -2) / mt.factorial(i)
        a.append(p)
    return a


def create_mat(m_x_y, m_y, n):
    m = [[m_x_y[j][i] * 2 * m_y[i] for i in range(n)] for j in range(n)]
    return m


def entropy_p(m, n):
    h = 0
    for i in range(n):
        h += m[i] * mt.log2(m[i])
    return -h


def entropy(m, n):
    h = 0
    for i in range(n):
        for j in range(n):
            h += m[i][j] * mt.log2(m[i][j])
    return -h


def sum_m(m):
    a = 0
    for i in m:
        a += i
    return a


def print_m(m):
    c = 0
    a = 0
    for i in m:
        a += sum(i)
        if c <= 9:
            print(i)
            c += 1
        else:
            print(*i)
    return a


num = 9

mat_x_y = create_m(num)
print("\nМатрица P(x/y):")
s = print_m(mat_x_y)
print("\nСумма всех элементов P(x/y): ", round(s, 3))

mat_y_x = create_m(num)
print("\nМатрица P(y/x):")
s = print_m(mat_y_x)
print("\nСумма всех элементов P(y/x): ", round(s, 3))

mat_x = create_p_1(num)
s = sum_m(mat_x)
print("\nМатрица P(x):")
print(mat_x)
print("\nСумма всех элементов P(x): ", round(s))

mat_y = create_p_2(num)
s = sum_m(mat_y)
print("\nМатрица P(y):")
print(mat_y)
print("\nСумма всех элементов P(y): ", round(s))

mat = create_mat(mat_x_y, mat_y, num)
print("\nМатрица P(x,y):")
s = print_m(mat)
print("\nСумма всех элементов P(x,y): ", round(s))
h = entropy(mat, num)
print("\nЭнтропия H(x,y): ", round(h, 3))
h_x = entropy_p(mat_x, num)
print("\nЭнтропия H(x): ", round(h_x, 3))
h_y = entropy_p(mat_y, num)
print("\nЭнтропия H(y): ", round(h_y, 3))
h_x_y = h - h_y
print("\nЭнтропия H(x/y): ", round(h_x_y, 3))
h_y_x = h - h_x
print("\nЭнтропия H(y/x): ", round(h_y_x, 3))
print("\nКоличество информации I(x,y): ", round(h * num, 3))
c = num * (mt.log2(9) - h_x_y)
print("\nПропускная способность: ", round(c, 3))
