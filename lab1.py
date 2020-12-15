import time

class Lab1:

	def __init__(self, convert, b):
		self.convert = convert
		self.b = b

	def small_to_large(self):
		num_hex = input('Print your number:\n')
		num_b = self.convert.hex_to_b(num_hex)
		print(num_b)

	def add(self):
		num_hex_1 = input('Print your first number:\n')
		num_hex_2 = input('Print your second number:\n')
		num_b_1 = self.convert.hex_to_b(num_hex_1)
		num_b_2 = self.convert.hex_to_b(num_hex_2)
		time_start = time.time()
		num_b_3 = self.add_long(num_b_1, num_b_2, self.b)
		time_end = time.time()
		print("Time: " + str(time_end - time_start))
		num_hex_3 = self.convert.b_to_hex(num_b_3)
		print(num_hex_3)

	def add_long(self, num_b_1, num_b_2, extent):
		if len(num_b_2) > len(num_b_1):
			x = num_b_1
			num_b_1 = num_b_2
			num_b_2 = x
		num_b_3 = []
		num_b_1.reverse()
		num_b_2.reverse()
		carry = 0
		for i in range(len(num_b_1)):
			second = 0
			if len(num_b_2) > i:
				second = num_b_2[i]
			temp = num_b_1[i] + second + carry
			num_b_3.append(temp % extent)
			carry = temp // extent
		if carry != 0:
			num_b_3.append(carry)
		num_b_3.reverse()
		return num_b_3
		
	def sub(self):
		num_hex_1 = input('Print your first number:\n')
		num_hex_2 = input('Print your second number:\n')
		num_b_1 = self.convert.hex_to_b(num_hex_1)
		num_b_2 = self.convert.hex_to_b(num_hex_2)
		if not self.cmp_long(num_b_1, num_b_2):
			print('Negative number')
			return
		time_start = time.time()
		num_b_3 = self.sub_long(num_b_1, num_b_2, self.b)
		time_end = time.time()
		print("Time: " + str(time_end - time_start))
		num_hex_3 = self.convert.b_to_hex(num_b_3)
		print(num_hex_3)

	def sub_long(self, num_b_1, num_b_2, extent):
		num_b_3 = []
		num_b_1.reverse()
		num_b_2.reverse()
		borrow = 0
		for i in range(len(num_b_1)):
			second = 0
			if len(num_b_2) > i:
				second = num_b_2[i]
			temp = num_b_1[i] - second - borrow
			if temp >= 0:
				num_b_3.append(temp)
				borrow = 0
			else:
				num_b_3.append(temp + extent)
				borrow = 1
		num_b_3.reverse()
		while(len(num_b_3) != 0):
			if num_b_3[0] == 0:
				del num_b_3[0]
			else:
				break
		return num_b_3

	def mul_one_digit(self, num_b, a, extent):
		num_b.reverse()
		carry = 0
		num_b_result = []
		for i in range(len(num_b)):
			temp = num_b[i] * a + carry
			num_b_result.append(temp % extent)
			carry = temp // extent
		if carry != 0:
			num_b_result.append(carry)
		num_b_result.reverse()
		num_b.reverse()
		return num_b_result

	def shift(self, num, count):
		new_num = num.copy()
		for i in range(count):
			new_num.append(0)
		return new_num
			
	def mul(self):
		num_hex_1 = input('Print your first number:\n')
		num_hex_2 = input('Print your second number:\n')
		num_b_1 = self.convert.hex_to_b(num_hex_1)
		num_b_2 = self.convert.hex_to_b(num_hex_2)
		time_start = time.time()
		num_b_3 = self.mul_long(num_b_1, num_b_2, self.b)
		time_end = time.time()
		print("Time: " + str(time_end - time_start))
		num_hex_3 = self.convert.b_to_hex(num_b_3)
		print(num_hex_3)

	def mul_long(self, num_b_1, num_b_2 , extent):
		if len(num_b_2) > len(num_b_1):
			x = num_b_1
			num_b_1 = num_b_2
			num_b_2 = x
		num_b_3 = []
		num_b_2.reverse()
		for i in range(len(num_b_2)):
			temp = self.mul_one_digit(num_b_1, num_b_2[i], extent)
			temp = self.shift(temp, i)
			num_b_3 = self.add_long(temp, num_b_3,extent)
		return num_b_3
		
	def sqr(self):
		num_hex_1 = input('Print your number:\n')
		num_b_1 = self.convert.hex_to_b(num_hex_1)
		num_b_2 = num_b_1.copy()
		num_b_3 = self.mul_long(num_b_1, num_b_2, self.b)
		num_hex_3 = self.convert.b_to_hex(num_b_3)
		print(num_hex_3)

	def cmp_long(self, num_b_1, num_b_2):
		while(len(num_b_1) != 0):
			if num_b_1[0] == 0:
				del num_b_1[0]
			else:
				break
		while(len(num_b_2) != 0):
			if num_b_2[0] == 0:
				del num_b_2[0]
			else:
				break
		if len(num_b_1) > len(num_b_2):
			return True
		elif len(num_b_1) < len(num_b_2):
			return False
		else:
			for i in range(len(num_b_1)):
				if num_b_1[i] > num_b_2[i]:
					return True
				if num_b_1[i] < num_b_2[i]:
					return False
			return True #equal

	def insert(self, num_bin, position):
		if len(num_bin) <= position:
			num_bin.append(1)
			num_bin = self.shift(num_bin, position)
		else:
			num_bin.reverse()
			num_bin[position] = 1
			num_bin.reverse()
		return num_bin

	def div(self):
		num_hex_1 = input('Print your first number:\n')
		num_hex_2 = input('Print your second number:\n')
		num_b_1 = self.convert.hex_to_b(num_hex_1)
		num_b_2 = self.convert.hex_to_b(num_hex_2)
		num_bin_1 = self.convert.b_to_bin(num_b_1)
		num_bin_2 = self.convert.b_to_bin(num_b_2)
		time_start = time.time()
		div = self.div_long(num_bin_1, num_bin_2)
		time_end = time.time()
		print("Time: " + str(time_end - time_start))
		num_bin_3 = div[0]
		num_bin_4 = div[1]
		num_hex_3 = self.convert.bin_to_hex(num_bin_3)
		num_hex_4 = self.convert.bin_to_hex(num_bin_4)
		print(num_hex_3)
		print(num_hex_4)

	def div_long(self, num_bin_1, num_bin_2):
		k = len(num_bin_2)
		R = num_bin_1
		Q = []
		while self.cmp_long(R,num_bin_2):
			t = len(R)
			C = self.shift(num_bin_2, t-k)
			if not (self.cmp_long(R,C)):
				t -= 1
				C = self.shift(num_bin_2, t-k)
			R = self.sub_long(R, C, 2)
			Q = self.insert(Q, t-k)
		return [Q,R]

	def power(self):
		num_hex_1 = input('Print your first number:\n')
		num_hex_2 = input('Print your second number:\n')
		num_b_1 = self.convert.hex_to_b(num_hex_1)
		num_b_2 = self.convert.hex_to_b(num_hex_2)
		num_bin_1 = self.convert.b_to_bin(num_b_1)
		num_bin_2 = self.convert.b_to_bin(num_b_2)
		time_start = time.time()
		num_bin_3 = self.power_long(num_bin_1, num_bin_2)
		time_end = time.time()
		print("Time: " + str(time_end - time_start))
		num_hex_3 = self.convert.bin_to_hex(num_bin_3)
		print(num_hex_3)

	def power_long(self, num_bin_1, num_bin_2):
		num_bin_3 = [1]
		num_bin_2.reverse()
		for symbol in num_bin_2:
			print("1")
			if symbol == 1:
				num_bin_3 = self.mul_long(num_bin_3, num_bin_1, 2)
			num_bin_1 = self.mul_long(num_bin_1.copy(), num_bin_1, 2)
		return num_bin_3

	def test1(self):
		num_hex_1 = input('Print your first number:\n')
		num_hex_2 = input('Print your second number:\n')
		num_hex_3 = input('Print your third number:\n')
		num_b_1 = self.convert.hex_to_b(num_hex_1)
		num_b_2 = self.convert.hex_to_b(num_hex_2)
		num_b_3 = self.convert.hex_to_b(num_hex_3)

		num_b_12sum = self.add_long(num_b_1, num_b_2, self.b)
		num_b_12sum3 = self.mul_long(num_b_12sum, num_b_3, self.b)

		num_b_312sum = self.mul_long(num_b_3, num_b_12sum, self.b)

		num_b_13 = self.mul_long(num_b_1, num_b_3, self.b)
		num_b_23 = self.mul_long(num_b_2, num_b_3, self.b)
		num_b_sum123 = self.add_long(num_b_13, num_b_23, self.b)

		num_hex_12sum3 = self.convert.b_to_hex(num_b_12sum3)
		num_hex_312sum = self.convert.b_to_hex(num_b_312sum)
		num_hex_sum123 = self.convert.b_to_hex(num_b_sum123)
		print(num_hex_12sum3)
		print(num_hex_312sum)
		print(num_hex_sum123)
		if (num_hex_12sum3 == num_hex_312sum and num_hex_312sum == num_hex_sum123):
			print("OK!")

	def test2(self):
		num_hex_1 = input('Print your first(N) number:\n')
		num_hex_2 = input('Print your second(A) number:\n')
		num_b_1 = self.convert.hex_to_b(num_hex_1)
		num_b_2 = self.convert.hex_to_b(num_hex_2)
		num_b_na = self.mul_long(num_b_1, num_b_2, self.b)
		num_dec_1 = self.convert.hex_to_dec(num_hex_1)
		num_b_sum = []
		for i in range(num_dec_1):
			num_b_sum = self.add_long(num_b_sum, num_b_2, self.b)
		num_hex_na = self.convert.b_to_hex(num_b_na)
		num_hex_sum = self.convert.b_to_hex(num_b_sum)
		print(num_hex_na)
		print(num_hex_sum)
		if (num_hex_na == num_hex_sum):
			print("OK!")