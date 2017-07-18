#!/usr/local/bin/python3

# we can overload the operator with predefined numerical operators
class NumBox:
def __init__(self, num):
self.Num = num
def __add__(self, num):
self.Num += num
def __sub__(self, num):
self.Num -= num
def __radd__(self,num):
self.Num += num

n = NumBox(40)

# should not change the order of operands

n + 100
print (n.Num)
n -100
print (n.Num)

100 + n
print (n.Num)
