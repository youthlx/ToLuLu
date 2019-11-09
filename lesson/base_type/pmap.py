# -*- coding:utf-8 -*-
# author xin.luo

# dict字典,存储键值对,可以通过键获取值,用{'xx': xx, 'xx': xx, ...}定义
d = {'female': 0, 'male': 1}
print(d)

# 向字典中插入键值对
d['female doctor'] = 2
print(d)

# 删除键值对，如果想删除键值对的时候还要获取对应的值可以采用pop
# del d['female doctor']直接删，不返回值
new_sex = d.pop('female doctor')
print(d)
print(new_sex)

# 将一个dict更新到另外一个dict中使用update，如果有重复的键，那么值会被新的覆盖，否则直接加入新的
# 键值对到源dict中
new_d = {'hello': 'world', 'male': 2}
d.update(new_d)
print(d)

# 根据键获取值
# 如果很确定这个dict里面一定有这个键可以使用[]取值如下
male_code = d['male']
print(male_code)
# 如果不确定可以使用get取值，第一个参数是键，
# 第二个参数是如果dict里面没有这个键，就返回它作为默认值Z
maybe_val = d.get('hello', '')
unknown_val = d.get('baba', 'is not you')
print(maybe_val)
print(unknown_val)

