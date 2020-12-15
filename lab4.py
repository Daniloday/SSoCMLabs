import time
from lab1 import *
from convert import *


class Lab4:

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
        time_start = time.time()
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
        time_end = time.time()
        print("Time: " + str(time_end - time_start))
        c_str = self.convert.bin_to_str(c)
        return c_str

    def add_long(self,a,b):
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
        return c

    def mul(self,a_str,b_str):
        a = self.convert.str_to_bin(a_str)
        b = self.convert.str_to_bin(b_str)
        time_start = time.time()
        c = self.mul_long(a,b,2)
        d = self.div_long(c, self.p)[1]
        while(len(d) > self.m):
            del d[0]
        time_end = time.time()
        print("Time: " + str(time_end - time_start))
        d_str = self.convert.bin_to_str(d)
        return d_str

    def sqr(self,a_str):
        a = self.convert.str_to_bin(a_str)
        time_start = time.time()
        b = self.sqr_long(a)
        time_end = time.time()
        print("Time: " + str(time_end - time_start))
        b_str = self.convert.bin_to_str(b)
        return b_str
    
    def sqr_long(self,a):
        a.insert(0,a[len(a) - 1])
        del a[len(a) - 1]
        return a

    def power(self,a_str,n_str):
        n = self.convert.str_to_bin(n_str)
        a = self.convert.str_to_bin(a_str)
        time_start = time.time()
        c = [1]
        n.reverse()
        for i in range(len(n)):
            if n[i] == 1:
                c = self.mul_long(c.copy(),a.copy(),2)
                c = self.div_long(c.copy(), self.p)[1]
            a = self.sqr_long(a.copy())
            a = self.div_long(a.copy(), self.p)[1]
        time_end = time.time()
        print("Time: " + str(time_end - time_start))
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
            num_b_3 = self.add_long(temp, num_b_3)
        
        return num_b_3
    
    def div_long(self, num_bin_1, num_bin_2):
        k = len(num_bin_2)
        R = num_bin_1
        Q = []
        while self.lab1.cmp_long(R,num_bin_2):
            t = len(R)
            C = self.lab1.shift(num_bin_2, t-k)
            R = self.add_long(R, C)
            Q = self.lab1.insert(Q, t-k)
            while(len(R) != 0):
                if R[0] == 0:
                    del R[0]
                else:
                    break
        return [Q,R]
    
    def inverted(self,a_str):
        a = self.convert.str_to_bin(a_str)
        m = len(a)
        n = 2 ** m - 2
        n_bin = self.convert.dec_to_bin(n)
        n_str = self.convert.bin_to_str(n_bin)
        pw = self.power(a_str,n_str)
        return pw

    def trace(self,a_str):
        a = self.convert.str_to_bin(a_str)
        time_start = time.time()
        m = len(a)
        trace = [0]
        for i in range(m):
            trace = self.add_long(trace.copy(),a.copy())
            a = self.sqr_long(a.copy())
        time_end = time.time()
        print("Time: " + str(time_end - time_start))
        return self.convert.bin_to_str(trace)

    def test1(self,a_str,b_str,c_str):
        a = self.convert.str_to_bin(a_str)
        b = self.convert.str_to_bin(b_str)
        c = self.convert.str_to_bin(c_str)

        aplusb = self.add_long(a.copy(),b.copy())
        abc = self.mul_long(aplusb,c.copy(),2)

        ac = self.mul_long(a.copy(),c.copy(),2)
        bc = self.mul_long(b.copy(),c.copy(),2)
        abc2 = self.add_long(ac,bc)

        if(abc == abc2):
            return "OK!"
        else:
            return "NO!"

    def test2(self,a_str):
        a = self.convert.str_to_bin(a_str)
        m = len(a) 
        n = 2 ** m - 1
        n_bin = self.convert.dec_to_bin(n)
        n_str = self.convert.bin_to_str(n_bin)
        pw = self.power(a,n_str)
        return pw

def main():
    lab4 = Lab4()
    a = input("A:\n")
    b = input("B:\n")
    n = input("N:\n")
    print("A + B:")
    print(lab4.add(a,b))
    # print("A * B:")
    # print(lab3.mul(a,b))
    print("A ^ 2:")
    print(lab4.sqr(a))
    # print("A ^ (-1):")
    # print(lab4.inverted(a))
    # print("A ^ N:")
    # print(lab3.power(a,n))
    print("Trace A:")
    print(lab4.trace(a))
    # print("Test 1:")
    # print(lab3.test1(a,b,n))
    # print("Test 2:")
    # print(lab3.test2(a))

if __name__ == '__main__':
    main()