#!/usr/bin/python3

dic = {'name':'Smith', 'rank':1, 'average':97.5}
print (type(dic))

print (dic['name'])
print (dic['rank'])

dic = {'a':'b', 'c':'d', 'e':'f'}
del dic['a']
print (dic);

dic = {'name':'Smith', 'phone':'01131313131', 'age':18}
print (dic.keys())

for i in dic.keys():
    print(i)

print (dic.values())

print (dic.items())

dic.clear()
print (dic)

dic = {'name':'Smith', 'phone':'01131313131', 'age':18}
print (dic.get('phone'))

print ('name' in dic)
