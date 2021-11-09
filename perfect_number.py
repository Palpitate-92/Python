# -*- coding: utf-8 -*-
# perfect_number.py
# @author Suyi
# @email suyi067113@gmail.com
# @description 找出1w以内的完美数，完美数又称为完全数或完备数，它的所有的真因子（即除了自身以外的因子）的和（即因子函数）恰好等于它本身。
# @created 2021-06-19T23:41:01.936Z+08:00
# @last-modified 2021-06-20T01:14:23.170Z+08:00
#

from math import sqrt
import time

time_start = time.time()
for i in range(1, 10000):
    perfect_judge = i
    for j in range(1, i):
        if i % j == 0:
            perfect_judge -= j
        if perfect_judge < 0:
            break
    if perfect_judge == 0:
        print(i)
time_end = time.time()
print('time cost: ', time_end - time_start, 's')
