#!/usr/local/bin/python3

class Student:
name = "김철수"
def info (self):
print ("제 이름은" + self.name + "입니다")

inst = Student()
print (type(inst))
print (inst.name)
inst.info()

class Dog:
name = "멍멍이"
def cry(self):
print (self.name + ": 왈왈")

dog = Dog()
dog.cry()
