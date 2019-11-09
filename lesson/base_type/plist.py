# -*- coding:utf-8 -*-
# author xin.luo

# 重头戏来了，list，中文我们称之为列表, tuple，我们称之为不可变列表
# list里面的元素用,分割，最后还可以带个,（当然也可以不带）代表可能有其他元素要加进来
num_list = [1, 2, 3, 4, 5, ]
str_list = ['上', '山', '打', '老', '虎', ]
print(num_list)
print(str_list)

# 向list中添加元素
num_list.append(6)
str_list.append('哈哈')
print(num_list)
print(str_list)

# 向一个list中添加另外一个list
num_list.extend(str_list)
print(num_list)

# tuple用()括起来，一旦定义，不能添加或者删除里面的元素
fix_tuple = (1, 2, 3, 4)
print(fix_tuple)
