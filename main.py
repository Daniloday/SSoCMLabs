from convert import *
from lab1 import *
from lab2 import *


def main():
    b = int(2 ** 64)
    convert = Convert(b)
    lab1 = Lab1(convert, b)
    lab2 = Lab2(convert, b)
    while True:
        # print("Choose option:\n1. Small to large \n2. Add \n3. Sub \n4. Mul \n5. Sqr \n6. Div \n7. Power\n8. Test1\n9. Test2 \nN/n to quit" )
        # choose = input()
        # if choose == '1':
        #     lab1.small_to_large()
        # if choose == '2':
        #     lab1.add()
        # if choose == '3':
        #     lab1.sub()
        # if choose == '4':
        #     lab1.mul()
        # if choose == '5':
        #     lab1.sqr()
        # if choose == '6':
        #     lab1.div()
        # if choose == '7':
        #     lab1.power()
        # if choose == '8':
        #     lab1.test1()
        # if choose == '9':
        #     lab1.test2()
        print("Choose option:\n1. GCD \n2. LCM \n3. Add \n4. Sub \n5. Mul \n6. Sqr \n7. Power\n8. Test1\n9. Test2 \nN/n to quit" )
        choose = input()
        if choose == '1':
            lab2.gcd()
        if choose == '2':
            lab2.lcm()
        if choose == '3':
            lab2.add()
        if choose == '4':
            lab2.sub()
        if choose == '5':
            lab2.mul()
        if choose == '6':
            lab2.sqr()
        if choose == '7':
            lab2.power()
        if choose == '8':
            lab2.test1()
        if choose == '9':
            lab2.test2()
        if choose == 'n' or choose == 'N':
            break

if __name__ == '__main__':
	main()