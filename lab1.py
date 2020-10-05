import math


class Convert:

	def __init__(self, b):
		self.b = b

	def convert_symbol_to_dec(self, symbol):

		if symbol == 'A':
			return 10
		elif symbol == 'B':
			return 11
		elif symbol == 'C':
			return 12
		elif symbol == 'D':
			return 13
		elif symbol == 'E':
			return 14
		elif symbol == 'F':
			return 15
		else:
			return int(symbol)

	def convert_dec_to_symbol(self, dec):
		if dec == 10:
			return 'A'
		elif dec == 11:
			return 'B'
		elif dec == 12:
			return 'C'
		elif dec == 13:
			return 'D'
		elif dec == 14:
			return 'E'
		elif dec == 15:
			return 'F'
		else:
			return str(dec)

	def hex_to_dec(self, num):
		num = num[::-1]
		num_dec = 0
		order = 0
		for symbol in num:
			num_dec += self.convert_symbol_to_dec(symbol) * int(pow(16, order))
			order += 1
		return num_dec

	def b_to_dec(self, num_b):
		num_b.reverse()
		num_dec = 0
		order = 0
		for symbol in num_b:
			num_dec += symbol * int(self.b ** order)
			order += 1
		return int(num_dec)

	def hex_to_b(self,num_hex):
		num_dec = self.hex_to_dec(num_hex)
		num_b = []
		while(True):
			num_b.append((num_dec % self.b))
			num_dec //= self.b
			if num_dec == 0:
				break
		num_b.reverse()
		return num_b 

	def b_to_hex(self, num_b):
		num_dec = self.b_to_dec(num_b)
		return self.dec_to_hex(num_dec)

	def dec_to_hex(self, num_dec):
		num_hex = ''
		while(True):
			num_hex += self.convert_dec_to_symbol((num_dec % 16))
			num_dec //= 16
			if num_dec == 0:
				break
		num_hex = num_hex[::-1]
		return num_hex

	def b_to_bin(self, num_b):
		num_bin = []
		for order in num_b:
			temp = []
			for i in range(int(math.log2(self.b))):
				temp.append((order % 2))
				order //= 2
			temp.reverse()
			num_bin += temp
		while(len(num_bin) != 0):
			if num_bin[0] == 0:
				del num_bin[0]
			else:
				break
		return num_bin

	def bin_to_hex(self, num_bin):
		num_bin.reverse()
		num_dec = 0
		order = 0
		for symbol in num_bin:
			num_dec += symbol * int(2 ** order)
			order += 1
		return self.dec_to_hex(num_dec)



	

class Exercises:

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
		num_b_3 = self.add_long(num_b_1, num_b_2, self.b)
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
		num_b_3 = self.sub_long(num_b_1, num_b_2, self.b)
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
		num_b_3 = self.mul_long(num_b_1, num_b_2, self.b)
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
		div = self.div_long(num_bin_1, num_bin_2)
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
		return (Q,R)

	def power(self):
		num_hex_1 = input('Print your first(A) number:\n')
		num_hex_2 = input('Print your second(N) number:\n')
		num_b_1 = self.convert.hex_to_b(num_hex_1)
		num_b_2 = self.convert.hex_to_b(num_hex_2)
		num_bin_1 = self.convert.b_to_bin(num_b_1)
		num_bin_2 = self.convert.b_to_bin(num_b_2)
		num_bin_3 = self.power_long(num_bin_1, num_bin_2)
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

	def test(self):
		num_hex_1 = input('Print your first number:\n')
		num_b_1 = self.convert.hex_to_b(num_hex_1)
		print(num_b_1)
		a = self.convert.b_to_bin(num_b_1)
		print(a)
		
		


def main():
	b = int(2 ** 64)
	convert = Convert(b)
	exercises = Exercises(convert, b)
	while True:
		print("Choose option:\n1. Small to large \n2. Add \n3. Sub \n4. Mul \n5. Sqr \n6. Div \n7. Power \nN/n to quit" )
		choose = input()
		if choose == '1':
			exercises.small_to_large()
		if choose == '2':
			exercises.add()
		if choose == '3':
			exercises.sub()
		if choose == '4':
			exercises.mul()
		if choose == '5':
			exercises.sqr()
		if choose == '6':
			exercises.div()
		if choose == '7':
			exercises.power()
		if choose == '8':
			exercises.test()
		if choose == 'n' or choose == 'N':
			break
	

if __name__ == '__main__':
	main()