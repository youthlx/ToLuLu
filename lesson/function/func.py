# -*- coding:utf-8 -*-
# author xin.luo

# 这里介绍下函数，
# 函数就是把一系列操作结合在一起以提供重用并代表某类动作的标识
# 格式如下：function_name为你自己定义的方法名称， params为参数，返回使用return
# def function_name(params):
#     do sth
#     return or not

# 现在来看一个加法的样例, 在这个样例中可以看到
# function_name是sum, 参数是a和b，
# 可以发现python因为是弱类型语言，所以在定义a和b的时候并没有指明他们是什么类型，
# 但是你在定义这个函数的时候要清楚这个a和b应该是什么类型，或者说可以是什么类型
# 这里有返回值返回两者的和，返回可以用return来提出
def sum(a, b):
	return a + b
total = sum(1, 2)
print('%s + %s = %s' % (1, 2, total))
# 函数其实也是一种类型，当然函数也就可以做为变量，比如现在我们给sum函数取个别名叫add
add = sum
total = add(1, 2)
print(total)

# 我们来看一个不返回任何东西的函数, 比如和一个人打招呼
def greeting(name):
	print('hello ' + name)
print('下面这个是一个不返回任何值得函数')
greeting('penglu')

# 我们在来看一个没有任何参数但是有返回值得函数，比如输出99乘法表
def nine_x_nine():
	table = ''
	for i in range(1, 10):
		for j in range(i, 10):
			table += ('%sx%s=%s ' % (i, j, i*j))
		table += '\n'
	return table
mul_nine_nine = nine_x_nine()
print(mul_nine_nine)

# 通过上述的范例可以清楚的知道函数名是基本上要有的
# （其实也可以没有，后面要讲匿名函数）,
# 参数可有可无，可以返回也可以不返回值

# 如果函数写到一半发现不会写了，但是如果不写它又报错怎么办呢，可以使用pass
# pass的意思就是好了，我懵逼了，等我清醒的时候再来看看吧
def do_complex_thing():
	print('此时才思泉涌....')
	print('pi ba pi ba打码中...')
	print('哦豁，懵逼了，不会写了，怎么办呢，先停一下让我pass一下吧')
	pass

# 那么我写了很多函数，但是我又不想让其立即运行，有没有一个程序的入口函数呢，当然
# main就是这个入口函数他有固定的格式，如下
if __name__ == '__main__':
	do_complex_thing()
