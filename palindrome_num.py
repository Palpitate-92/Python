# -*- coding: utf-8 -*-
# Reversal_int.py
# @author Suyi
# @email suyi067113@gmail.com
# @description 判断输入的数是不是回文数
# @created 2021-06-19T22:55:12.398Z+08:00
# @last-modified 2021-06-20T23:35:09.791Z+08:00
#


def is_palindrome(num):
    """判断一个数是不是回文数，tmp可实现正整数的翻转"""
    total = 0
    tmp = num
    while tmp > 0:
        total = total * 10 + tmp % 10
        tmp //= 10
    return total == num


if __name__ == '__main__':
    num = str(input('请输入一个数: '))
    while num != '0':
        if num == num[::-1]:  #is_palindrome(num) == True:
            print(f'{num}是一个回文数')
        else:
            print('%s不是一个回文数' % num)
        num = str(input('请输入一个数: '))
