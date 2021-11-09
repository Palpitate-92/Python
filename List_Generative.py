# -*- coding: utf-8 -*-
# List_Generative.py
# @author Suyi
# @email suyi067113@gmail.com
# @description 列表的生成式和生成器
# @created 2021-06-21T13:11:14.371Z+08:00
# @last-modified 2021-06-21T13:30:37.811Z+08:00
#
#
import sys

# 我们还可以使用列表的生成式语法来创建列表，代码如下所示。
f = [x for x in range(1, 10)]
print(f)
f = [x + y for x in 'ABCDE' for y in '1234567']
print(f)
# 用列表的生成表达式语法创建列表容器
# 用这种语法创建列表之后元素已经准备就绪所以需要耗费较多的内存空间
f = [x**2 for x in range(1, 1000)]
print(sys.getsizeof(f))  # 查看对象占用内存的字节数
print(f)
# 请注意下面的代码创建的不是一个列表而是一个生成器对象
# 通过生成器可以获取到数据但它不占用额外的空间存储数据
# 每次需要数据的时候就通过内部的运算得到数据(需要花费额外的时间)
f = (x**2 for x in range(1, 1000))
print(sys.getsizeof(f))  # 相比生成式,生成器不占用存储数据的空间
print(f)
for val in f:
    print(val)
#
'''除了上面提到的生成器语法，Python中还有另外一种定义生成器的方式，就是通过`yield`关键字将一个普通函数改造成生成器函数'''


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


def main():
    for val in fib(20):
        print(val)


if __name__ == '__main__':
    main()