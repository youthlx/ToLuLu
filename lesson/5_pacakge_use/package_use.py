# -*- coding:utf-8 -*-
# author xin.luo

# python之美在于很多东西别人都写好了，你只需要导入然后使用就可以了
# 导入的方式有两种一种是直接import,另外一种是from import
# 来，让我们看看时间函数的使用

# 直接使用import package，在调用的时候需要package.function使用
# 比如下面输出时间戳
import time

now = time.time()
print(now)

# 如果使用from package import subpackage/function可以不用加package.
from datetime import date
today = date.today()
print(today)
# 这里就输入from package import subpackage的格式，
# 我们没有用datetime.date.today(0而是直接用subpackage.function也就是date.today()来表示
