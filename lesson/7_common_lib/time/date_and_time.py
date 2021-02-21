# -*- coding:utf-8 -*-
# author xin.luo
from datetime import datetime

# 日期
# 当前时间
now = datetime.now()
print(now)
print(type(now))
# 任意时间 (2021年2月22日上午1点2分3秒4毫秒)
anytime = datetime(2021, 2, 22, 1, 2, 3, 4)
print(anytime.date())
print(anytime.time())


# 日期时间类型转换
# 字符串转时间
t2 = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(t2)
# 时间转字符串
print(t2.strftime('%a, %b %d %H:%M'))
# 时间转时间戳
tm = t2.timestamp()
print(tm)
# 时间戳转时间
tt = datetime.fromtimestamp(tm)
print(tt)