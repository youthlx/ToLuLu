# -*- coding:utf-8 -*-
# author xin.luo

# 基本类型bool
a = True
b = False
print(type(a), a)
print(type(b), b)
# 运算
and_result = a and b
or_result = a or b
not_result = not a
print('%s and %s -> %s' % (a, b, and_result))
print('%s or %s -> %s' % (a, b, or_result))
print('not %s -> %s' % (a, not_result))
