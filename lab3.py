import time
from lab1 import *
from convert import *


class Lab3:

    def __init__(self):
        self.m = 179
        self.p_str = "100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010111"
        # self.m = 3
        # self.p_str = "1011"
        self.convert = Convert(2)
        self.p = self.convert.str_to_bin(self.p_str)
        self.lab1 = Lab1(self.convert, 2)

    def add(self,a_str,b_str):
        a = self.convert.str_to_bin(a_str)
        b = self.convert.str_to_bin(b_str)
        if len(b) > len(a):
            x = a
            a = b
            b = x
        c = []
        a.reverse()
        b.reverse()
        for i in range(len(a)):
            second = 0
            if len(b) > i:
                second = b[i]
            bit = (a[i] + second) % 2
            c.append(bit)
        c.reverse()
        c_str = self.convert.bin_to_str(c)
        return c_str

    def mul(self,a_str,b_str):
        a = self.convert.str_to_bin(a_str)
        b = self.convert.str_to_bin(b_str)
        c = self.mul_long(a,b,2)
        d = self.div_long(c, self.p)[1]
        while(len(d) > self.m):
            del d[0]
        d_str = self.convert.bin_to_str(d)
        return d_str

    def power(self,a_str,n_str):
        n = self.convert.str_to_bin(n_str)
        a = self.convert.str_to_bin(a_str)
        # for i in range(len(power)-1):
        #     c = power.insert(i*2+1,0)
        #     power_str = self.div_long(c, self.p)[1]
        c = [1]
        n.reverse()
        for i in range(len(n)):
            if n[i] == 1:
                c = self.mul_long(c.copy(),a.copy(),2)
                c = self.div_long(c.copy(), self.p)[1]
            a = self.mul_long(a.copy(),a.copy(),2)
            a = self.div_long(a.copy(), self.p)[1]
        return self.convert.bin_to_str(c)


    def mul_long(self, num_b_1, num_b_2 , extent):
        if len(num_b_2) > len(num_b_1):
            x = num_b_1
            num_b_1 = num_b_2
            num_b_2 = x
        num_b_3 = []
        num_b_2.reverse()
        for i in range(len(num_b_2)):
            temp = self.lab1.mul_one_digit(num_b_1, num_b_2[i], extent)
            temp = self.lab1.shift(temp, i)
            num_b_3 = self.convert.str_to_bin(self.add(temp, num_b_3))
        
        return num_b_3
    
    def div_long(self, num_bin_1, num_bin_2):
        k = len(num_bin_2)
        R = num_bin_1
        Q = []
        while self.lab1.cmp_long(R,num_bin_2):
            t = len(R)
            C = self.lab1.shift(num_bin_2, t-k)
            R = self.convert.str_to_bin(self.add(self.convert.bin_to_str(R), self.convert.bin_to_str(C)))
            Q = self.lab1.insert(Q, t-k)
            while(len(R) != 0):
                if R[0] == 0:
                    del R[0]
                else:
                    break
        return [Q,R]
    
        



def main():
    lab3 = Lab3()
    a = input("A:\n")
    b = input("B:\n")
    n = input("N:\n")
    print("A + B:")
    print(lab3.add(a,b))
    print("A * B:")
    print(lab3.mul(a,b))
    print("A ^ 2:")
    print(lab3.mul(a,a))
    print("A ^ N:")
    print(lab3.power(a,n))


if __name__ == '__main__':
    main()