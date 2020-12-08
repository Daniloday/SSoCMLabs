import time
from lab1 import *
from lab2 import *

class Lab3:

    def __init__(self, convert, b):
        self.convert = convert
        self.b = b
        self.lab1 = Lab1(self.convert, self.b)
        self.lab2 = Lab1(self.convert, self.b)