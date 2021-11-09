# -*- coding: utf-8 -*-
# Fibonacci.py
# @author Suyi
# @email suyi067113@gmail.com
# @description 生成Fibonacci数列
# @created 2021-06-19T23:32:16.944Z+08:00
# @last-modified 2021-06-19T23:32:28.098Z+08:00
#

num_Fibonacci = int(input('需要生成的斐波拉契数列的位数为: '))
Fibonacci = 0
pre_Fibonacci = 0
two_Fibonacci = 0
for _ in range(num_Fibonacci):
    Fibonacci = pre_Fibonacci + two_Fibonacci
    if (Fibonacci == 0):
        Fibonacci = 1
    #将pre_Fibonacci的值赋给two_Fibonacci，将Fibonacci的值赋给pre_Fibonacci
    two_Fibonacci, pre_Fibonacci = pre_Fibonacci, Fibonacci
    print(Fibonacci)