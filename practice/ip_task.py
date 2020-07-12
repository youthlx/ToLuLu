import unittest


def is_ip_address(addr):
	if '.' in addr and ':' not in addr:
		return is_ipv4(addr)
	elif '.' not in addr and ':' in addr:
		return is_ipv6(addr)
	else:
		return False


def is_ipv4(v4_address):
	"""
	判断是否为ipv4地址
	:param v4_address:
	:return:
	"""
	ip_segments = v4_address.split('.')
	# ipv4的地址为四段
	if len(ip_segments) != 4:
		return False
	for segment in ip_segments:
		# 每段最长不能超过4个，最大为255
		if len(segment) > 3:
			return False
		# 每段必须为数字
		if not segment.isdigit():
			return False
		num = int(segment)
		# 每段必须在0-255之间
		if num < 0 or num > 255:
			return False
	return True


def is_ipv6(v6_address):
	"""
	判断是否为ipv6地址
	:param v6_address:
	:return:
	"""
	ip_segments = v6_address.split(':')
	# ipv6最多8段，以冒号分割
	if len(ip_segments) > 8:
		return False
	omit_count = 0
	for segment in ip_segments:
		if segment == '':
			omit_count += 1
			# 省略0不能超过两次
			if omit_count > 1:
				return False
			continue
		if segment == '0':
			continue
		# 除0外必须是小于4个16进制字符组成
		if len(segment) > 4:
			return False
		# 16进制以数字0-9和字母a-f表示
		if not segment.isalnum():
			return False
		# 16进制字母必须在a-f之间
		if segment.isalpha():
			for al in segment:
				if al not in ['A', 'B', 'C', 'D', 'E', 'F', 'a', 'b', 'c', 'd', 'e', 'f']:
					return False
	return True


class TestIsIPAddress(unittest.TestCase):

	def test_ip_address(self):
		self.assertFalse(is_ip_address("aaaaaaaaaabbbbbbbb"))

		self.assertFalse(is_ip_address("127.0.0.1.2"))
		self.assertFalse(is_ip_address("1234.0.0.1"))
		self.assertFalse(is_ip_address("a.b.0.c"))
		self.assertFalse(is_ip_address("256.0.0.1"))
		self.assertFalse(is_ip_address("127.0.0.-1"))
		self.assertTrue(is_ip_address("127.0.0.1"))

		self.assertFalse(is_ip_address("FF60::2A90:FA:0:4CA2:9C5A:0:A"))
		self.assertFalse(is_ip_address("FF60::2A90:FA:0:4CA2:9C5A::"))
		self.assertFalse(is_ip_address("FF60::2A90:ABCDDD:0:4CA2:9C5A:0"))
		self.assertFalse(is_ip_address("FF60::2A90:FA*(:0:4CA2:9C5A:0"))
		self.assertFalse(is_ip_address("FF60::2A90:FH:0:4CA2:9C5A:0"))
		self.assertTrue(is_ip_address("FF60::2A90:FA:0:4CA2:9C5A:0"))


if __name__ == '__main__':
	unittest.main()