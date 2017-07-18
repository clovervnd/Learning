\#!\/usr\/local\/bin\/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3
#!/usr/local/bin/python3

class Book:
def __init__(self,bookName):
self.name = bookName
print("객체가 생성되었습니다. 책의 이름은 "+bookName+"입니다.")

objectBook = Book("열혈 C++ 프로그래밍")

class IceCream:
def __init__(self, name, price):
self.name = name
self.price = price
print (name+"의 가격은 "+str(price)+"원 입니다.")
def __del__(self):
print (self.name + " 객체가 소멸합니다.")

objectIc=IceCream("월드콘", 1000)

del objectIc
