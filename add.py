# -*- coding: utf-8 -*-
# add.py
# @author Suyi
# @email suyi067113@gmail.com
# @description
# @created 2021-06-20T13:19:19.203Z+08:00
# @last-modified 2021-06-20T13:33:28.689Z+08:00
#


# 在参数名前面的*表示args是一个可变参数
def add(*args):
    total = 0
    for val in args:
        """在args里面取值"""
        total += val
    return total


# 在调用add函数时可以传入0个或多个参数
# __name__是Python中一个隐含的变量它代表了模块的名字
# 只有被Python解释器直接执行的模块的名字才是__main__
# 也就是说在其他文件将该文件作为模块导入时，不会运行下面的语句
if __name__ == '__main__':
    print(add())
    print(add(1))
    print(add(1, 2))
    print(add(1, 2, 3))
    print(add(3, 2, 1))
    print(add(1, 4, 7, 2, 5, 6, 3, 4, 8, 11))
"""
form module import foo 从module文件导入函数foo(),如要调用该foo()函数，直接使用foo()
import module as m1    导入mudole文件，将其重命名为m1，如要调用module文件里的foo()函数，则使用m1.foo()
from module import foo as m1 从module文件导入函数foo()，如要调用该foo()函数，只能使用m1()
"""