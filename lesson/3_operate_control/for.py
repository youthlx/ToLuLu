# -*- coding:utf-8 -*-
# author xin.luo

# for，while是用于遍历的，或者理解为循环操作，主要针对两种数据类型，一种是list/tuple，一种是dict
# 它的基本格式是
# for item in items:
#     do sth for item
# 下面我们分别对list/tuple和dict来做遍历
# 遍历list
WEEK = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
for day in WEEK:
	print(day)

# 遍历dict
CHINESE_WEEK = {
	'Monday': '星期一',
	'Tuesday': '星期二',
	'Wednesday': '星期三',
	'Thursday': '星期四',
	'Friday': '星期五',
	'Saturday': '星期六',
	'Sunday': '星期日'
}
# 如果直接遍历dict的话，遍历的是它的键
for key in CHINESE_WEEK:
	print(key, '=', CHINESE_WEEK[key])
# 当然我们也可以直接遍历dict的键值对，需要借助dict的items方法，
# 如下(和上面是一样的结果)
for key, val in CHINESE_WEEK.items():
	print(key, '=', val)


# 有两个小知识点这里需要了解一下
# 生成从0到n-1的序列，可以使用range(n),range的其他用法可以网上搜素一下
for i in range(10):
	print(i)
# 字符串str类型也是可以遍历的,可以把它理解为字符的list
statement = 'aya, wo shuai dao le'
print('statem的第一个字符是', statement[0])
print('statement的长度是: ', len(statement))
for c in statement:
	print(c)

# continue用来跳过循环，break用来中断循环
# 可以想象一下，下面这个循环会输出什么
example = [1, 2, 3, 4, 5]
for i in example:
	if i == 2:
		continue
	if i == 4:
		break
	print(i)

# while相关的用法可自行搜素，并不常用
