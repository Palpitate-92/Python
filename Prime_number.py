# -*- coding: utf-8 -*-
# Prime_number.py
# @author Suyi
# @email suyi067113@gmail.com
# @description 判断输入数字是否是素数
# @created 2021-06-19T10:32:31.591Z+08:00
# @last-modified 2021-06-20T14:19:34.672Z+08:00
#

from math import sqrt


def is_prime(num):
    """判断一个数是不是素数"""
    end = int(sqrt(num))
    for factor in range(2, end + 1):
        if num % factor == 0:
            return False
    return True if num != 1 else False


if __name__ == '__main__':
    while True:
        num = int(input("请输入一个正整数: "))
        #if is_prime and num != 1:  #相当于(is_prime)and(num != 1)，而类似于A<B<C则相当于(A<B)and(B<C)
        if is_prime(num):
            print(f'{num}是素数')
        else:
            print(f'{num}不是素数')
