# -*- coding:utf-8 -*-
# author xin.luo

# 函数第二课：使用默认参数
# 什么叫默认参数呢，其实就是调用函数时如果参数没有传的话，会使用默认设置的值，来，举个栗子
# 下面这个是计算base的time次方，假如base=2， time=3，就是2^3,=8
def power(base, time):
	result = 1
	for i in range(time):
		result *= base
	return result


result = power(2, 3)
print("2的3次方（不使用默认函数 =", result)

# 我们都知道其实大家很关注一个数的平方，但是又希望这个函数不仅仅可以计算一个数的平方
# 那么怎么做呢，看下面
def power2(base, time=2):
	result = 1
	for i in range(time):
		result *= base
	return result
result2 =power2(3)
print("3的平方（使用默认函数）=", result2)
# 你会返现这个函数的实现和上面的没有任何区别唯一不同的地方是time参数后面跟了=2，这就是默认参数
# 在调用的时候如果不传time参数，会默认使用time=2来集计算