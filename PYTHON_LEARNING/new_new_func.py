\#!\/usr\/local\/bin\/python3
\#!\/usr\/local\/bin\/python3
\#!\/usr\/local\/bin\/python3
\#!\/usr\/local\/bin\/python3
\#!\/usr\/local\/bin\/python3
\#!\/usr\/local\/bin\/python3
\#!\/usr\/local\/bin\/python3
\#!\/usr\/local\/bin\/python3
\#!\/usr\/local\/bin\/python3
\#!\/usr\/local\/bin\/python3
\#!\/usr\/local\/bin\/python3
\#!\/usr\/local\/bin\/python3
\#!\/usr\/local\/bin\/python3
\#!\/usr\/local\/bin\/python3
\#!\/usr\/local\/bin\/python3
\#!\/usr\/local\/bin\/python3
\#!\/usr\/local\/bin\/python3
\#!\/usr\/local\/bin\/python3
\#!\/usr\/local\/bin\/python3
\#!\/usr\/local\/bin\/python3
\#!\/usr\/local\/bin\/python3
\#!\/usr\/local\/bin\/python3
\#!\/usr\/local\/bin\/python3
\#!\/usr\/local\/bin\/python3
\#!\/usr\/local\/bin\/python3
\#!\/usr\/local\/bin\/python3
\#!\/usr\/local\/bin\/python3
\#!\/usr\/local\/bin\/python3
\#!\/usr\/local\/bin\/python3
\#!\/usr\/local\/bin\/python3
\#!\/usr\/local\/bin\/python3
\#!\/usr\/local\/bin\/python3
\#!\/usr\/local\/bin\/python3
\#!\/usr\/local\/bin\/python3
\#!\/usr\/local\/bin\/python3
\#!\/usr\/local\/bin\/python3
\#!\/usr\/local\/bin\/python3
\#!\/usr\/local\/bin\/python3
\#!\/usr\/local\/bin\/python3
\#!\/usr\/local\/bin\/python3
\#!\/usr\/local\/bin\/python3
\#!\/usr\/local\/bin\/python3
\#!\/usr\/local\/bin\/python3
\#!\/usr\/local\/bin\/python3
\#!\/usr\/local\/bin\/python3
\#!\/usr\/local\/bin\/python3
\#!\/usr\/local\/bin\/python3
\#!\/usr\/local\/bin\/python3
\#!\/usr\/local\/bin\/python3
\#!\/usr\/local\/bin\/python3
\#!\/usr\/local\/bin\/python3
\#!\/usr\/local\/bin\/python3
\#!\/usr\/local\/bin\/python3
\#!\/usr\/local\/bin\/python3
\#!\/usr\/local\/bin\/python3
\#!\/usr\/local\/bin\/python3
\#!\/usr\/local\/bin\/python3
\#!\/usr\/local\/bin\/python3
\#!\/usr\/local\/bin\/python3
\#!\/usr\/local\/bin\/python3
\#!\/usr\/local\/bin\/python3
\#!\/usr\/local\/bin\/python3
\#!\/usr\/local\/bin\/python3
\#!\/usr\/local\/bin\/python3
\#!\/usr\/local\/bin\/python3
\#!\/usr\/local\/bin\/python3
\#!\/usr\/local\/bin\/python3
\#!\/usr\/local\/bin\/python3
\#!\/usr\/local\/bin\/python3
\#!\/usr\/local\/bin\/python3
\#!\/usr\/local\/bin\/python3
\#!\/usr\/local\/bin\/python3
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

def absolute(n):
if n<0:
n = -n
return n

print (-3)
print (absolute(-3))

def mul_div(a,b):
return a*b, a/b

print (mul_div(4,5))

n = 10
def func():
global n
n = n*10
func()
print (n)

def func(*var1):
for i in var1:
print (i, end=' ')

func(1,2,3)
func(2,4,6,6,1,23)


# default value should be set at the last varialbe
def mul(a, b=10):
return a*b

print (mul(3))
print (mul(3,2))
