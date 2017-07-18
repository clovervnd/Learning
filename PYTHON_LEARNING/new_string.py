#!/usr/local/bin/python3

weight = 78.5
print("WEIGHT:", format(weight, '.1f'))
print("MONEY:", format(12931401,',d'))

print ('{} {}'.format("gildong", 34))

print ('{0} {1} {2}'.format(12, 34, 56))
print ('{2} {2} {1} {0}'.format(12, 34, 56))

print ('{0} / {1} = {2:.4f}'.format(13, 3, 13/3));

lst = [30, 40, 50, 80, 90, 100];
print ('lst[4] = {0[4]}'.format(lst))

print ('My age is {age}, my weight is {weight}'.format(age = 25, weight = 78.5))

print ('{0:6s}'.format('cat'))
print ('{0:5d}'.format(335))

print ('{0:<6d}'.format(1234))
print ('{0:>6d}'.format(1234))

print ('{0:07}'.format(1234))

print ('{0:#o} {0:#x}'.format(123))

s = 'adFqdwDqw'
print (s.upper())
print (s.lower())

s = "It's always such a pleasure"
print (s.find('way'))
print (s.find('the'))

s = "we are invincible, we are unique"
print (s.count('we'))
print (s.count('in'))

s = 'AB-C-D-EFGH'
s = s.replace('-', '')
print (s)

s = '             1234 56      '
s = s.strip()
print (s)

s = '1/2/3/4/5/6'
lst = s.split('/')
print (lst[3])

