# -*- coding: utf-8 -*-
# 100_Chickens.py
# @author Suyi
# @email suyi067113@gmail.com
# @description 白鸡百笼问题
# @created 2021-06-19T23:00:27.551Z+08:00
# @last-modified 2021-06-19T23:01:34.541Z+08:00
#

for x in range(20):
    for y in range(33):
        z = 100 - x - y
        if x * 5 + y * 3 + z / 3 == 100:
            print(f'公鸡{x}只，母鸡{y}只，小鸡{z}只')