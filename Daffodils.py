# -*- coding: utf-8 -*-
# Daffodils.py
# @author Suyi
# @email suyi067113@gmail.com
# @description 在100到1000中寻找水仙花数
# @created 2021-06-19T22:28:29.598Z+08:00
# @last-modified 2021-06-19T22:47:56.409Z+08:00
#

for num in range(100, 1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if low**3 + mid**3 + high**3 == num:
        print(num)