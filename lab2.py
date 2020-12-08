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

	def add(self):
		num_hex_1 = input('Print your first number:\n')
		num_hex_2 = input('Print your second number:\n')
		num_hex_3 = input('Print your mod number:\n')
		num_b_1 = self.convert.hex_to_b(num_hex_1)
		num_b_2 = self.convert.hex_to_b(num_hex_2)
		num_b_3 = self.convert.hex_to_b(num_hex_3)
		num_bin_3 = self.convert.b_to_bin(num_b_3)
		time_start = time.time()
		num_bin_5 = self.add_long(num_b_1,num_b_2,num_bin_3)
		num_hex_5 = self.convert.bin_to_hex(num_bin_5)
		time_end = time.time()
		print("Time: " + str(time_end - time_start))
		print(num_hex_5)

	def add_long(self,num_b_1, num_b_2, num_bin_3):
		num_b_4 = self.lab1.add_long(num_b_1, num_b_2, self.b)
		num_bin_4 = self.convert.b_to_bin(num_b_4)
		m = 2 ** len(num_bin_4)
		m1 = self.convert.dec_to_bin(m)
		m = self.lab1.div_long(m1,num_bin_3)[0]
		num_bin_5 = self.barrettReduction(num_bin_4, num_bin_3,m)
		return num_bin_5

	def sub(self):
		num_hex_1 = input('Print your first number:\n')
		num_hex_2 = input('Print your second number:\n')
		num_hex_3 = input('Print your mod number:\n')
		num_b_1 = self.convert.hex_to_b(num_hex_1)
		num_b_2 = self.convert.hex_to_b(num_hex_2)
		num_b_3 = self.convert.hex_to_b(num_hex_3)
		num_bin_3 = self.convert.b_to_bin(num_b_3)
		time_start = time.time()
		num_bin_5 = self.sub_long(num_b_1,num_b_2,num_bin_3)
		num_hex_5 = self.convert.bin_to_hex(num_bin_5)
		time_end = time.time()
		print("Time: " + str(time_end - time_start))
		print(num_hex_5)

	def sub_long(self,num_b_1, num_b_2, num_bin_3):
		num_b_4 = self.lab1.sub_long(num_b_1, num_b_2, self.b)
		num_bin_4 = self.convert.b_to_bin(num_b_4)
		m = 2 ** len(num_bin_4)
		m1 = self.convert.dec_to_bin(m)
		m = self.lab1.div_long(m1,num_bin_3)[0]
		num_bin_5 = self.barrettReduction(num_bin_4, num_bin_3,m)
		return num_bin_5

	def mul(self):
		num_hex_1 = input('Print your first number:\n')
		num_hex_2 = input('Print your second number:\n')
		num_hex_3 = input('Print your mod number:\n')
		num_b_1 = self.convert.hex_to_b(num_hex_1)
		num_b_2 = self.convert.hex_to_b(num_hex_2)
		num_b_3 = self.convert.hex_to_b(num_hex_3)
		num_bin_3 = self.convert.b_to_bin(num_b_3)
		time_start = time.time()
		num_bin_5 = self.mul_long(num_b_1, num_b_2, num_bin_3)
		num_hex_5 = self.convert.bin_to_hex(num_bin_5)
		time_end = time.time()
		print("Time: " + str(time_end - time_start))
		print(num_hex_5)

	def mul_long(self,num_b_1, num_b_2, num_bin_3):
		num_b_4 = self.lab1.mul_long(num_b_1, num_b_2, self.b)
		num_bin_4 = self.convert.b_to_bin(num_b_4)
		m = 2 ** len(num_bin_4)
		m1 = self.convert.dec_to_bin(m)
		m = self.lab1.div_long(m1,num_bin_3)[0]
		num_bin_5 = self.barrettReduction(num_bin_4, num_bin_3,m)
		return num_bin_5

	def barrettReduction(self, x, n, m):
		q = self.killLastDigits(x.copy(), len(n) - 1)
		q = self.lab1.mul_long(q, m, 2)
		q = self.killLastDigits(x.copy(), len(n) + 1)
		r = self.lab1.sub_long(x.copy(),self.lab1.mul_long(q.copy(),n.copy(),2), 2)
		return self.lab1.div_long(x,n)[1]
		

	def killLastDigits(self, x , k):
		if x != None:
			return x
		for i in range(k):
			del x[-i+1]
		return x

	def power(self):
		num_hex_1 = input('Print your first number:\n')
		num_hex_2 = input('Print your second number:\n')
		num_hex_3 = input('Print your mod number:\n')
		num_bin_1 = self.convert.hex_to_bin(num_hex_1)
		num_bin_2 = self.convert.hex_to_bin(num_hex_2)
		num_bin_3 = self.convert.hex_to_bin(num_hex_3)
		time_start = time.time()
		num_bin_4 = self.gorner(num_bin_1, num_bin_2, num_bin_3)
		num_hex_4 = self.convert.bin_to_hex(num_bin_4)
		time_end = time.time()
		print("Time: " + str(time_end - time_start))
		print(num_hex_4)

	def sqr(self):
		num_hex_1 = input('Print your first number:\n')
		num_hex_3 = input('Print your mod number:\n')
		num_bin_1 = self.convert.hex_to_bin(num_hex_1)
		num_bin_3 = self.convert.hex_to_bin(num_hex_3)
		time_start = time.time()
		num_bin_4 = self.gorner(num_bin_1, [1,0], num_bin_3)
		num_hex_4 = self.convert.bin_to_hex(num_bin_4)
		time_end = time.time()
		print("Time: " + str(time_end - time_start))
		print(num_hex_4)

	def gorner(self, A, B, n):
		C = [1]
		m = 2 ** (len(n)*2)
		m1 = self.convert.dec_to_bin(m)
		m = self.lab1.div_long(m1,n)[0]
		B.reverse()
		for i in range(len(B)):
			if B[i] == 1:
				C = self.barrettReduction(self.lab1.mul_long(C.copy(),A.copy(),2), n, m)
			A = self.barrettReduction(self.lab1.mul_long(A.copy(),A.copy(),2), n, m)
		return C

	def test1(self):
		num_hex_1 = input('Print your first number:\n')
		num_hex_2 = input('Print your second number:\n')
		num_hex_3 = input('Print your third number:\n')
		num_hex_mod = input('Print your mod number:\n')

		num_b_1 = self.convert.hex_to_b(num_hex_1)
		num_b_2 = self.convert.hex_to_b(num_hex_2)
		num_b_3 = self.convert.hex_to_b(num_hex_3)
		num_bin_mod = self.convert.hex_to_bin(num_hex_mod)

		num_bin_12sum = self.add_long(num_b_1.copy(), num_b_2.copy(), num_bin_mod.copy())
		num_b_12sum = self.convert.bin_to_b(num_bin_12sum.copy())
		num_bin_12sum3 = self.mul_long(num_b_12sum.copy(), num_b_3.copy(), num_bin_mod.copy())
		num_bin_312sum = self.mul_long(num_b_3.copy(), num_b_12sum.copy(), num_bin_mod.copy())

		num_bin_13 = self.mul_long(num_b_1.copy(), num_b_3.copy(), num_bin_mod.copy())
		num_bin_23 = self.mul_long(num_b_2.copy(), num_b_3.copy(), num_bin_mod.copy())
		num_b_13 = self.convert.bin_to_b(num_bin_13)
		num_b_23 = self.convert.bin_to_b(num_bin_23)
		num_bin_sum123 = self.add_long(num_b_13.copy(), num_b_23.copy(), num_bin_mod.copy())

		num_hex_12sum3 = self.convert.bin_to_hex(num_bin_12sum3)
		num_hex_312sum = self.convert.bin_to_hex(num_bin_312sum)
		num_hex_sum123 = self.convert.bin_to_hex(num_bin_sum123)
		if (num_hex_12sum3 == num_hex_312sum and num_hex_312sum == num_hex_sum123):
			print("OK!")
		else:
			print("NO!")

	def test2(self):
		num_hex_1 = input('Print your first(N) number:\n')
		num_hex_2 = input('Print your second(A) number:\n')
		num_hex_mod = input('Print your mod number:\n')
		num_b_1 = self.convert.hex_to_b(num_hex_1)
		num_b_2 = self.convert.hex_to_b(num_hex_2)
		num_bin_mod = self.convert.hex_to_bin(num_hex_mod)

		num_bin_na = self.mul_long(num_b_1.copy(), num_b_2.copy(), num_bin_mod)

		num_dec_1 = self.convert.hex_to_dec(num_hex_1)
		num_b_sum = []
		for i in range(num_dec_1):
			num_bin_sum = self.add_long(num_b_sum.copy(), num_b_2.copy(), num_bin_mod.copy())
			num_b_sum = self.convert.bin_to_b(num_bin_sum.copy())
		num_hex_na = self.convert.bin_to_hex(num_bin_na)
		num_hex_sum = self.convert.bin_to_hex(num_bin_sum)
		print(num_hex_na)
		print(num_hex_sum)
		if (num_hex_na == num_hex_sum):
			print("OK!")
		else:
			print("No!")
		