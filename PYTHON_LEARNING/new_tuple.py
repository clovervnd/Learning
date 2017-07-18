#!/usr/local/bin/python3

tuples = (1,2,3,4,5)
print (type(tuples))

a,b = 10, 20
print (a,b)

a,b=b,a
print(a,b)

# we can index and slice tuple
tuples = (0,1,2,3,4,5,6)
print (tuples[1])
print (tuples[2:4])

tuples = ('a', 'b', 'c')
print (tuples + ('d', 'e', 'f'))
print (tuples*3)
