# -*- coding:utf-8 -*-
# author xin.luo

# 这里我们要说的是分支控制语句, 什么叫分支控制呢，就是如果...， 如果又...， 否则...
# 格式是 if condition:
#            do sth
#        elif condition:
#            do other sth
#        else:
#            do rest sth
# 给个小例子，如果考试得了90分以上算优秀，如果得了80分以上算良好，
# 得了60分以上算合格， 得了60分以下算不及格

# 这里要学习一个新的技能，接受命令行输入，我们使用input，但是记住接受输入的是字符串
# 由于是字符串，但是我们需要的是整数，所以需要强转
print('请输入你的考试分数, 按回车结束')
score = input()
score = int(score)
if score >= 90:
	print('Excellent')
elif score >= 80:
	print('Good')
elif score >= 60:
	print('Pass')
else:
	print('Not Pass')

# 当然如果不需要使用elif也可去掉，比如以下
if score >= 60:
	print('你及格了哟')
else:
	print('你不及格呦')