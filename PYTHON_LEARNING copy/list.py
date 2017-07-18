#!/usr/bin/python3

lst = [1, 2, 5, 'a', 'b']
print (lst)
print (type(lst))

lst = [1,2,'a','b','red','beaf', ['a', 'b', 'c']]
print (lst[-2])
print (lst[1:3])
# 끝 숫자는 범위에서 뺀다

lst = [1,2,'a','b','red','breaf']
lst[2] = 3
lst[4] = 'blue'

print (lst)

lst1 = ['A', 'B', 'C']
lst2 = ['D', 'E', 'F']

print(lst1+lst2)

fruit = ['apple', 'banana', 'pineapple']
fruit.append('grape')
print (fruit)

lst = ['A', 'B', 1, 2, 3.14, 10.16]
lst.append([1,2,3])
print (lst)

lst = [1,2,4,5,6]
lst.insert(2,3)
print (lst)

nums = [1,2,3,4,5,6]
nums.extend([7,8,9])
print (nums)

lst = ['red', 'blue', 'green', 'yellow', 'white', 'black', 'blue']
print (lst.index('blue'))
print (lst.index('blue',2))
print (lst.index('yellow', 2,4))

lst = [1,1,2,3,4,5,6,6,6,7]
print (lst.count(1))

a = [1,2,1,3,4,1]
a.remove(1)
print (a)

a = [3,5,1,2,7]
a.sort()
print(a)

a = [1,3,5,7,9]
a.reverse()
print (a)
