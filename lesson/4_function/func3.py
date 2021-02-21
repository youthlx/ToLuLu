# -*- coding:utf-8 -*-
# author xin.luo

# 这一节我们来说说可变参数， 上面叫可变参数呢，试想一下这样的场景
# 现在要自动输出一个人的简历， 简历上有联系方式一栏，但是现在一个人
# 的联系方式是在太多了，有电话，邮箱，qq， 微信等等，怎么办，来看看
def output_contact(*args):
	print("我的联系方式有三种：\n")
	print("第一种：%s" % args[0])
	print("第一种：%s" % args[1])
	print("第一种：%s" % args[2])

output_contact("luoxin199203@163.com", "15625587502", "1003109590")

# *args就是一种代表一串信息的参数，使用场景是你不确定或者参数太多
# 写不过来的时候，他的本质是list，可以用args[0], args[1],...,args[n]
# 表示，没有上限，但是要注意的是*args和不可变参数可以共存，但是必须
# 写在不可变参数的最后，看下面的栗子
def mix_contact(email, *args):
	print("这是我的邮箱%s，+:\n" % email)
	print("第一种：%s" % args[0])
	print("第一种：%s" % args[1])
mix_contact("luoxin199203@163.com", "15625587502", "1003109590")

# 下一个更重要的可变参数叫做*kwargs,它代表一个dict，那么他的使用场景
# 是什么呢？想象一下现在简历里要写姓名，学校，技能啥的，而且还要技能
# 的熟悉度，我去，我tm会的东西多了去了，咋办没关系，咱有**kwags，
# 看下下面的栗子
def output_info(**kwargs):
	print("我叫%s\n" % kwargs.get("name", ""))
	print("我毕业于%s\n" % kwargs.get("university", ""))
	print("我会python%s\n" % kwargs.get("python", ""))
	print("我会java%s\n" % kwargs.get("java", ""))
	print("我会golang%s\n" % kwargs.get("golang", ""))

output_info(name="罗欣", university="华南理工大学", python="叼的飞起", java="跟我比这个，叫爸爸", golang="还差点，很快搞定")
# 看使用的时候的格式是key=val是不是超简单的，而且键值对数量没有限制

# 代表一切参数的可变参数格式,看到下面这种参数格式代表这里的参数可以是任何你想设置的参数，我们称之为通用参数
def all(*args, **kwargs):
	pass
