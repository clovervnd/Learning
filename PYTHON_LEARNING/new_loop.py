#!/usr/local/bin/python3

i=1
while i <=10:
print (i, "번 출력되었습니다")
i += 1

i=1
while i<=10:
if i == 7:
break
print (i, "번 출력되었습니다")
i+=1

i=0
while i<=10:
i+=1
if i%2 ==1 :
continue
print (i, "번 출력되었습니다")

lst = [1,3,5,7,9]
for i in lst:
print (i)

for i in range(10):
print (i, end=" ")

print ("n",range(10))

lst = [1,2,3,4,5]
for i in range(len(lst)):
if i%2 == 0:
lst[i] *=2
else:
lst[i] *= -2
print(lst[i], end=" ")

