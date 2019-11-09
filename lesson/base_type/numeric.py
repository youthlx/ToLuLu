# -*- coding:utf-8 -*-
# author xin.luo

# python的注释是使用#符号的，和java的//是不同的
# 基本类型int, float
a = 1
b = 1.0
c = 1e2
d = 1e-2
# type函数返回值得类型
# 整型
print(type(a), a)
# 浮点型
print(type(b), b)
print(type(c), c)
print(type(d), d)
# 希望把整型转化为浮点型可以使用float(int)
# 希望把浮点型转化为整型可以使用int(float)
a1 = float(10)
a2 = int(1.3)
print(type(a1), a1)
print(type(a2), a2)
# 整型的加,减,乘,除,取整,取余,按位与
x = 5
y = 2
add = x + y
dec = x - y
mul = x * y
div = x / y
div2 = x // y
mod = x % y
bit_and = x & y
print('x = %s, y = %s' % (x, y))
print('x + y = %s' % add)
print('x - y = %s' % dec)
print('x * y = %s' % mul)
print('x / y = %s' % div)
print('x // y = %s' % div2)
print('x mod y = %s' % mod)
print('x & y = %s' % bit_and)
