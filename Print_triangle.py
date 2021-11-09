# -*- coding: utf-8 -*-
# Print_triangle.py
# @author Suyi
# @email suyi067113@gmail.com
# @description 打印三角图形
# @created 2021-06-19T20:14:04.018Z+08:00
# @last-modified 2021-06-19T22:48:36.651Z+08:00
#

row = 10  #int(input('请输入行数: '))
for i in range(row):
    for _ in range(i + 1):
        print('*', end='')
    print()

for i in range(row):
    for _ in range(row - i - 1):
        print(' ', end='')
    for _ in range(i + 1):
        print('*', end='')
    print()

for i in range(row):
    for _ in range(row - i - 1):
        print(' ', end='')
    for _ in range(i * 2 + 1):
        print('*', end='')
    print()