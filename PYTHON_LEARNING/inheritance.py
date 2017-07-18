#!/usr/bin/python3

class Person:
    def __init__(self, name, age, gender):
        self.Name = name
        self.Age = age
        self.Gender = gender
    def aboutMe(self):
        print ("저의 이름은: "+self.Name +"이구요, 제 나이는 " + self.Age + "살 입니다")

class Employee(Person):
    def __init__(self, name, age, gender, salary, hiredate):
        Person.__init__(self, name, age, gender)
        self.Salary = salary
        self.Hiredate = hiredate
    def doWork(self):
        print("열심히 일을 합니다.")
    def aboutMe(self):
        Person.aboutMe(self)
        print("제 급여는 "+ self.Salary + "원 이구요, 제 입사일은" + self.Hiredate + "입니다")
        
objectEmployee = Employee("김철수", "18", "남", "50000", "2013년 12월 29일")
objectEmployee.doWork()
objectEmployee.aboutMe()


class ParentOne:
    def func(self):
        print ("ParentOne의 함수 호출!")
class ParentTwo:
    def func(self):
        print ("ParentTwo의 함수 호출!")

class Child(ParentOne, ParentTwo):
    def childFunc(self):
        ParentOne.func(self)
        ParentTwo.func(self)

objectChild = Child()
objectChild.childFunc()

# func() from fore inherited ParentOne is executed
objectChild.func() 

class A:
    def __init__(self):
        print ("A 클래스의 생성자 호출!")
class B(A):
    def __init__(self):
        A.__init__(self)
        print ("B 클래스의 생성자 호출!")
class C(A):
    def __init__(self):
        A.__init__(self)
        print ("C 클래스의 생성자 호출!")
class D(B,C):
    def __init__(self):
        B.__init__(self)
        C.__init__(self)
        print ("D 클래스의 생성자 호출!")

objectA = D()

print("\n")

class A2:
    def __init__(self):
        print ("A 클래스의 생성자 호출!")
class B2(A2):
    def __init__(self):
        print ("B 클래스의 생성자 호출!")
        super().__init__()
class C2(A2):
    def __init__(self):
        print ("C 클래스의 생성자 호출!")
        super().__init__()
class D2(B2,C2):
    def __init__(self):
        print ("D 클래스의 생성자 호출!")
        super().__init__()

objectA2 = D2()


