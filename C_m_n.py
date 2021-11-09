# -*- coding: utf-8 -*-
# C_m_n.py
# @author Suyi
# @email suyi067113@gmail.com
# @description 求C_m_n
# @created 2021-06-20T13:07:37.493Z+08:00
# @last-modified 2021-06-20T13:08:58.185Z+08:00
#


def fac(num):
    """求阶乘"""
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result


m = int(input('请输入m: '))
n = int(input('请输入n: '))
print(fac(m) // fac(n) // fac(m - n))
