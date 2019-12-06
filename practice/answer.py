# -*- coding:utf-8 -*-
# author xin.luo


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


def decode_and_tidy(*args):
	cards = [puke_code[arg] for arg in args]
	cards.sort()
	return cards


def encode_card(*args):
	return [puke_code_reverse[arg] for arg in args]


def judge_type(*args):
	length = len(args)
	card_codes = decode_and_tidy(*args)
	if length == 1:
		return puke_type_single
	if length == 3:
		return puke_type_three_0

	if length == 2:
		if card_codes[0] == 17 and card_codes[1] == 18:
			puke_type = puke_type_boom
		else:
			puke_type = puke_type_pair
	elif length == 4:
		if card_codes[0] == card_codes[2] and card_codes[0] != card_codes[3]:
			puke_type = puke_type_three_1
		else:
			puke_type = puke_type_boom
	elif length == 5:
		if (card_codes[1] - card_codes[0]) == 1:
			puke_type = puke_type_series
		else:
			puke_type = puke_type_three_2
	else:
		puke_type = puke_type_series
	return puke_type


def have_boom_in_mine(card_list):
	cards = decode_and_tidy(*card_list)
	if 17 in cards and 18 in cards:
		return encode_card(17, 18)
	if len(cards) < 4:
		return []
	for i in range(len(cards) - 3):
		if cards[i] == cards[i + 3]:
			return encode_card(cards[i], cards[i], cards[i], cards[i])
	return []


def single_cover(enemy_cards, my_cards):
	boom_card = have_boom_in_mine(my_cards)
	if boom_card:
		return boom_card
	enemy_codes = decode_and_tidy(*enemy_cards)
	my_codes = decode_and_tidy(*my_cards)
	single_code = enemy_codes[0]
	for my_code in my_codes:
		if my_code > single_code:
			return encode_card(my_code)
	return []


def pair_cover(enemy_cards, my_cards):
	boom_card = have_boom_in_mine(my_cards)
	if boom_card:
		return boom_card
	enemy_codes = decode_and_tidy(*enemy_cards)
	my_codes = decode_and_tidy(*my_cards)
	greater_enemy = []
	for my_code in my_codes:
		if my_code > enemy_codes[0] and my_code in greater_enemy:
			return encode_card(my_code, my_code)
		greater_enemy.append(my_code)
	return []


def three_0_cover(enemy_cards, my_cards):
	boom_card = have_boom_in_mine(my_cards)
	if boom_card:
		return boom_card
	if len(my_cards) < 3:
		return []
	enemy_cards = decode_and_tidy(*enemy_cards)
	my_cards = decode_and_tidy(*my_cards)
	greater_enemy = []
	for i in range(len(my_cards) - 2):
		if my_cards[i] == my_cards[i + 2] and my_cards[i] > enemy_cards[0]:
			greater_enemy.append(my_cards[i])
	if len(greater_enemy) > 0:
		return encode_card(greater_enemy[0], greater_enemy[0], greater_enemy[0])
	else:
		return 0


def three_1_cover(enemy_cards, my_cards):
	boom_card = have_boom_in_mine(my_cards)
	if boom_card:
		return boom_card
	if len(my_cards) < 4:
		return []
	enemy_cards = decode_and_tidy(*enemy_cards)
	my_cards = decode_and_tidy(*my_cards)
	greater_enemy = []
	for i in range(len(my_cards) - 2):
		if my_cards[i] == my_cards[i + 2] and my_cards[i] > enemy_cards[1]:
			greater_enemy.append(my_cards[i])
	if len(greater_enemy) > 0:
		target_card = greater_enemy[0]
		diff_card = -1
		for my_card in my_cards:
			if my_card != target_card:
				diff_card = my_card
		return encode_card(target_card, target_card, target_card, diff_card)
	return []


def three_2_cover(enemy_cards, my_cards):
	boom_card = have_boom_in_mine(my_cards)
	if boom_card:
		return boom_card
	if len(my_cards) < 5:
		return []
	enemy_cards = decode_and_tidy(*enemy_cards)
	my_cards = decode_and_tidy(*my_cards)
	greater_enemy = []
	three_combine = []
	pair_combine = []
	for i in range(len(my_cards) - 2):
		if my_cards[i] == my_cards[i + 2] and my_cards[i] > enemy_cards[2]:
			three_combine.append(my_cards[i])
			greater_enemy.append(my_cards[i])
	if len(greater_enemy) > 0:
		for i in range(len(my_cards) - 1):
			if my_cards[i] == my_cards[i + 1]:
				pair_combine.append(my_cards[i])
		target_card = greater_enemy[0]
		diff_card = -1
		for pair_card in pair_combine:
			if pair_card != target_card:
				diff_card = pair_card
		if diff_card > 0:
			return encode_card(target_card, target_card, target_card, diff_card, diff_card)
		else:
			return []
	return []


def series_cover(enemy_cards, my_cards):
	boom_card = have_boom_in_mine(my_cards)
	if boom_card:
		return boom_card
	if len(my_cards) < len(enemy_cards):
		return []
	enemy_cards = decode_and_tidy(*enemy_cards)
	my_cards = decode_and_tidy(*my_cards)
	left = len(my_cards) - 2
	right = len(my_cards) - 1
	my_series_list = []
	while left >= 0 and right >= 0:
		left_val = my_cards[left]
		right_val = my_cards[right]
		if right_val - left_val == right - left:
			left = left - 1
		else:
			if right - left >= 5:
				my_series_list.append([right, right - left])
			right = left
			left = left - 1
	if right - left >= 5:
		my_series_list.append([right, right - left])
	for my_series in my_series_list:
		if my_cards[my_series[0]] > enemy_cards[len(enemy_cards) - 1] and my_series[1] >= len(enemy_cards):
			real_series = []
			count = 0
			for i in range(my_series[1]):
				count = count + 1
				if count > len(enemy_cards):
					break
				real_series.append(my_cards[my_series[0] - i])
			real_series.sort()
			return encode_card(*real_series)
	return []


def boom_cover(enemy_cards, my_cards):
	if 'black_joker' in enemy_cards:
		return []
	my_cards = decode_and_tidy(*my_cards)
	enemy_cards = decode_and_tidy(*enemy_cards)
	if 17 in my_cards and 18 in my_cards:
		return encode_card(17, 18)
	if len(my_cards) < 4:
		return []
	for i in range(len(my_cards) - 3):
		if my_cards[i] == my_cards[i + 3] and my_cards[i] > enemy_cards[0]:
			return encode_card(my_cards[i], my_cards[i], my_cards[i], my_cards[i])
	return []


def cover_you_or_not(enemy_cards, my_cards):
	puke_type = judge_type(*enemy_cards)
	if puke_type == puke_type_single:
		ret = single_cover(enemy_cards, my_cards)
	elif puke_type == puke_type_pair:
		ret = pair_cover(enemy_cards, my_cards)
	elif puke_type == puke_type_three_0:
		ret = three_0_cover(enemy_cards, my_cards)
	elif puke_type == puke_type_three_1:
		ret = three_1_cover(enemy_cards, my_cards)
	elif puke_type == puke_type_three_2:
		ret = three_2_cover(enemy_cards, my_cards)
	elif puke_type == puke_type_series:
		ret = series_cover(enemy_cards, my_cards)
	elif puke_type == puke_type_boom:
		ret = boom_cover(enemy_cards, my_cards)
	else:
		ret = []
	return ret, len(ret) > 0


if __name__ == '__main__':
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
