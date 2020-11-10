import time
from lab1 import *

class Lab2:

	def __init__(self, convert, b):
		self.convert = convert
		self.b = b
		self.lab1 = Lab1(self.convert, self.b)

	def gcd(self):
		num_hex_1 = input('Print your first number:\n')
		num_hex_2 = input('Print your second number:\n')
		num_b_1 = self.convert.hex_to_b(num_hex_1)
		num_b_2 = self.convert.hex_to_b(num_hex_2)
		num_bin_1 = self.convert.b_to_bin(num_b_1)
		num_bin_2 = self.convert.b_to_bin(num_b_2)
		time_start = time.time()
		num_bin_3 = self.gcd_long(num_bin_1,num_bin_2)
		num_hex_3 = self.convert.bin_to_hex(num_bin_3)
		time_end = time.time()
		print("Time: " + str(time_end - time_start))
		print(num_hex_3)

	def gcd_long(self, a, b):
		if not self.lab1.cmp_long(a, b):
			x = a.copy()
			a = b.copy()
			b = x
		d = [1]
		while a[-1] == 0 and b[-1] == 0:
			a = self.lab1.div_long(a, [1,0])[0]
			b = self.lab1.div_long(b, [1,0])[0]
			d = self.lab1.mul_long(d,[1,0], 2)
		while a[-1] == 0 :
			a = self.lab1.div_long(a, [1,0])[0]
			if a[0] == None:
				a.append(0)
		while b != [0]:
			while  b[-1] == 0 :
				b = self.lab1.div_long(b, [1,0])[0]
				if b[0] == None:
					b.append(0)
			if self.lab1.cmp_long(a, b):
				x = a.copy()
				a = b.copy()
				b = self.lab1.sub_long(x, b, 2)
			else:
				b = self.lab1.sub_long(b, a, 2)
			if len(b) == 0:
				b.append(0)
		d = self.lab1.mul_long(d,a, 2)
		return d
	
	def lcm(self):
		num_hex_1 = input('Print your first number:\n')
		num_hex_2 = input('Print your second number:\n')
		num_b_1 = self.convert.hex_to_b(num_hex_1)
		num_b_2 = self.convert.hex_to_b(num_hex_2)
		time_start = time.time()
		num_bin_1 = self.convert.b_to_bin(num_b_1)
		num_bin_2 = self.convert.b_to_bin(num_b_2)
		if not self.lab1.cmp_long(num_bin_1, num_bin_2):
			x = num_bin_1.copy()
			num_bin_1 = num_bin_2.copy()
			num_bin_2 = x
		gcd_bin = self.gcd_long(num_bin_1.copy(),num_bin_2.copy())
		num_bin_1 = self.lab1.div_long(num_bin_1, gcd_bin)[0]
		num_bin_3 = self.lab1.mul_long(num_bin_2, num_bin_1, 2)
		num_hex_3 = self.convert.bin_to_hex(num_bin_3)
		time_end = time.time()
		print("Time: " + str(time_end - time_start))
		print(num_hex_3)

		