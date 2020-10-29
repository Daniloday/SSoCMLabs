

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
