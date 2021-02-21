# -*- coding:utf-8 -*-
# author xin.luo

# 题目：斗地主
# 描述：我们在玩手机游戏斗地主的时候，常常有个按钮叫"提示"，
# 他会告诉你，你现有的手牌是要的起还是要不起，如果要的起，
# 要的起的牌是什么，如果要不起提示要不起
# 提示：分几个步骤去做这件事，
#     第一步理牌，就是把扑克牌按照牌型归类，顺子是顺子，三张是三张，一对是一对，单牌是单牌，炸弹是炸弹
#     第二步，判断别人出的牌是几张，除了炸弹特殊外，理论上别人出几张你也要出几张
#     第三步，根据别人出的牌型判断是否要的起要不起
# 下面这些是测试用例
puke_code = {
	'3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
	'J': 11, 'Q': 12, 'K': 13, 'A': 14, '2': 16, 'black_joker': 17, 'color_joker': 18,
}
puke_code_reverse = {
	3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10',
	11: 'J', 12: 'Q', 13: 'K', 14: 'A', 16: '2', 17: 'black_joker', 18: 'color_joker',
}

puke_type_single = 0
puke_type_pair = 1
puke_type_three_0 = 2
puke_type_three_1 = 3
puke_type_three_2 = 4
puke_type_series = 5
puke_type_boom = 6


def cover_you_or_not(*args):
	pass


if __name__ == '__main__':
	# 以下是测试用例，这些测试用例不完备，请补充
	print(cover_you_or_not(['3'], ['3', '4', '4', '4', '4', '5', '6']))
	print(cover_you_or_not(['4', '4'], ['3', '3', '3', '4', '4', '5', '7', '7']))
	print(cover_you_or_not(['9', '9', '9'], ['4', '10', '10', '10', 'J', 'J', 'J']))
	print(cover_you_or_not(['6', '6', '6', 'A'], ['7', '7', '7', 'Q', 'K']))
	print(cover_you_or_not(['7', '7', '7', 'J', 'J'], ['8', '8', '8', '9', '10', 'J']))
	print(cover_you_or_not(['7', '7', '7', 'J', 'J'], ['8', '8', '8', '9', '9', 'J']))
	print(cover_you_or_not(['7', '7', '7', 'K', 'K'], ['8', '8', '8', '9', '10', '10', '10']))
	print(cover_you_or_not(['A', 'A', 'A', 'A'], ['2', '2', '2', '2']))
	print(cover_you_or_not(['black_joker', 'color_joker'], ['3', '4', '5', '6', '7']))
	print(cover_you_or_not(['6', '7', '8', '9', '10', 'J'], ['3', '4', '5', '6', '7', '9', '10', 'J', 'Q', 'K', 'A']))