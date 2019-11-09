# -*- coding:utf-8 -*-
# author xin.luo

# 输出一行字符串在python中其实是有两种的，第一种是str，另外一种是unicode
# 可以看如下的样例,python的默认编码是unicode
str1 = '老欣欣好帅'
str2 = u'老欣欣好帅个毛线'
print('%s type: %s' % (str1, type(str1)))
print('%s type: %s' % (str2, type(str2)))

# 字符串的格式化和拼接
str1 = 'Hello,'
str2 = 'Beautiful LuLu'
s = str1 + str2
print('字符串的拼接=', s)
ss = '%s %s' % (str1, str2)
print('通过%s设置占位符来进行格式化,有几个%s就需要在后面写上多少个变量:%s', ss)

# 一些常规的字符串函数
s = ' &Big,Rabbit,Eat&xls'
print('全部变成大写=%s, 全部变成小写=%s' % (s.upper(), s.lower()))
print('按照符号切分成list，list是一种类型，后面会讲', s.split(','))
print('去除字符串前后空格', s.strip())
print('判断字符串是不是以什么字符结束(如果是开始用startswith)', s.endswith('xls'))
print('字符串的替换', s.replace('&', '@'))

# 判断一个字符串是不是在另外一个字符串中可以使用in，
# 返回一个bool类型，True代表在， False代表不在样例如下
s1 = 'Hello, LuLU'
is_in = 'Lu' in s1
print(is_in)