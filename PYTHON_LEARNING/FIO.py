#!/usr/local/bin/python3

f = open ('t.txt','w')
f.write('abcdefghijk')
f.close()

f = open ('t.txt', 'r')
print (f.read())
f.close()


f = open ('t.txt','w')
for i in range(1,10):
    data = "2 * %d = %d\n" % (i, 2*i)
    f.write(data)
f.close();

f = open('hangul.txt', 'w')
f.write('가나다\n라마바\n사아자\n차카타\n파하')
f.close()

f = open('hangul.txt', 'r')
print (f.tell())
print (f.read())
print (f.tell())
print (f.seek(0))
print (f.tell())
print (f.readline())
print (f.tell())
f.close()
