import time
from lab1 import *
from convert import *


class Lab4:

    def __init__(self):
        self.convert = Convert(2)
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
        d = self.mul_long(a,b)
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

    def createMatrix(self,a):
        m = len(a)
        p = 2 * m + 1
        matrix = []
        for i in range(m):
            matrix.append([])
            for j in range(m):
                if ((2 ** i) + (2 ** j)) % p == 1 or ((2 ** i) - (2 ** j)) % p == 1 or (-(2 ** i) + (2 ** j)) % p == 1 or (-(2 ** i) - (2 ** j)) % p == 1:
                    matrix[i].append(1)
                else:
                    matrix[i].append(0)
        return matrix

    def power(self,a_str,n_str):
        n = self.convert.str_to_bin(n_str)
        a = self.convert.str_to_bin(a_str)
        time_start = time.time()
        c = []
        for i in range(len(a)):
            c.append(1)
        n.reverse()
        for i in range(len(n)):
            if n[i] == 1:
                c = self.mul_long(c.copy(),a.copy())
            a = self.sqr_long(a.copy())
        time_end = time.time()
        print("Time: " + str(time_end - time_start))
        return self.convert.bin_to_str(c)

    def power_long(self,a,n):
        c = []
        for i in range(len(a)):
            c.append(1)
        n.reverse()
        for i in range(len(n)):
            if n[i] == 1:
                c = self.mul_long(c.copy(),a.copy())
            a = self.sqr_long(a.copy())
        return c

    def mul_long(self, a, b):
        matrix = self.createMatrix(a)
        d = []
        for k in range(len(a)):
            c = []
            for i in range(len(a)):
                sum = 0
                for j in range(len(a)):
                    sum += a[j] * matrix[j][i]
                c.append(sum % 2)
            sum = 0
            for i in range(len(c)):
                sum += c[i]*b[i]
            d.append(sum % 2)
            x = a[0]
            del a[0]
            a.append(x)
            y = b[0]
            del b[0]
            b.append(y)
        return d
     
    
    def inverted(self,a_str):
        a = self.convert.str_to_bin(a_str)
        time_start = time.time()
        m = len(a)
        n = m - 1
        n_bin = self.convert.dec_to_bin(n)
        k = 1
        b = a.copy()
        for i in range(len(n_bin)):
            if i == 0:
                continue
            c = self.sqr_long(b.copy())
            c = self.power_long(b.copy(),self.convert.dec_to_bin(2**k))
            b = self.mul_long(c.copy(),b.copy())
            k = 2*k
            if n_bin[i] == 1:
                b = self.sqr_long(b.copy())
                b = self.mul_long(b.copy(),a.copy())
                k += 1
        b = self.sqr_long(b.copy())
        time_end = time.time()
        print("Time: " + str(time_end - time_start))
        return self.convert.bin_to_str(b)

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
        abc = self.mul_long(aplusb,c.copy())

        ac = self.mul_long(a.copy(),c.copy())
        bc = self.mul_long(b.copy(),c.copy())
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
    print("A * B:")
    print(lab4.mul(a,b))
    print("A ^ 2:")
    print(lab4.sqr(a))
    print("A ^ (-1):")
    print(lab4.inverted(a))
    print("A ^ N:")
    print(lab4.power(a,n))
    print("Trace A:")
    print(lab4.trace(a))
    print("Test 1:")
    print(lab4.test1(a,b,n))
    print("Test 2:")
    print(lab4.test2(a))

if __name__ == '__main__':
    main()