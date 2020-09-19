from math import *


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
			num_dec += symbol * int(pow(self.b, order))
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
		num_hex = ''
		while(True):
			num_hex += self.convert_dec_to_symbol((num_dec % 16))
			num_dec //= 16
			if num_dec == 0:
				break
		num_hex = num_hex[::-1]
		return num_hex



	

class Exercises:

	def __init__(self, convert, b):
		self.convert = convert
		self.b = b

	def small_to_large(self):
		num_hex = input('Print your number:\n')
		num_b = self.convert.hex_to_b(num_hex)
		print(num_b)

	def addition(self):
		num_hex_1 = input('Print your first number:\n')
		num_hex_2 = input('Print your second number:\n')
		num_b_1 = self.convert.hex_to_b(num_hex_1)
		num_b_2 = self.convert.hex_to_b(num_hex_2)
		num_b_3 = []
		num_b_1.reverse()
		num_b_2.reverse()
		carry = 0
		for i in range(len(num_b_1)):
			temp = num_b_1[i] + num_b_2[i] + carry
			num_b_3.append(temp % self.b)
			carry = temp // self.b
		if carry != 0:
			num_b_3.append(carry)
		num_b_3.reverse()
		num_hex_3 = self.convert.b_to_hex(num_b_3)
		print(num_hex_3)
		
	def subtraction(self):
		num_hex_1 = input('Print your first number:\n')
		num_hex_2 = input('Print your second number:\n')
		num_b_1 = self.convert.hex_to_b(num_hex_1)
		num_b_2 = self.convert.hex_to_b(num_hex_2)
		num_b_3 = []
		num_b_1.reverse()
		num_b_2.reverse()
		borrow = 0
		for i in range(len(num_b_1)):
			temp = num_b_1[i] - num_b_2[i] - borrow
			if temp >= 0:
				num_b_3.append(temp)
				borrow = 0
			else:
				num_b_3.append(temp + self.b)
				borrow = 1
		num_b_3.reverse()
		num_hex_3 = self.convert.b_to_hex(num_b_3)
		print(num_hex_3)




		


def main():
	b = int(pow(2,64))
	convert = Convert(b)
	exercises = Exercises(convert, b)
	while True:
		print("Choose option: ")
		choose = input()
		if choose == '1':
			exercises.small_to_large()
		if choose == '2':
			exercises.addition()
		if choose == '3':
			exercises.subtraction()
		if choose == 'n' or choose == 'N':
			break
	

if __name__ == '__main__':
	main()