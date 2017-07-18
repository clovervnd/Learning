#!/usr/local/bin/python3

try:
a = 10/0
except ZeroDivisionError:
print ('제수는 0이 될 수 없습니다')

'''
try:
a = int(input("첫번째 숫자를 입력하세요: "))
b = int(input("두번째 숫자를 입력하세요: "))
print ("a + b = ", a+b)
except ValueError:
print("값이 적절하지 않습니다")

try:
a = int(input("피제수를 입력하세요: "))
b = int(input("제수를 입력하세요: "))
print("a / b = ", a / b)
except ValueError:
print('값이 적절하지 않습니다.')
except ZeroDivisionError:
print('제수는 0이 될 수 없습니다!')

try:
a = int(input("피제수를 입력하세요: "))
b = int(input("제수를 입력하세요: "))
print("a / b = ", a / b)
except (ValueError, ZeroDivisionError):
print("제수각 0이거나 값이 적절하지 않습니다.")
'''


try:
a = 50 / "이십"
except TypeError as e:
print ('예외:', e.args[0])

try:
f = open('test.txt', 'r')
except IOError:
print ('파일을 열지 못했습니다')
else:
print ('test.txt', f.read())
f.close()

try:
a=10/0
except ZeroDivisionError:
print ('제수는 0이 될 수 없습니다')
finally:
print ('무조건 실행되는 영역')

try:
a = int (input('피제수를 입력하세여: '))
b = int (input('제수를 입력하세요: '))
if a <= 0 or b<= 0:
raise ArithmeticError('피제수 혹은 제수가 0 이하일 수 없습니다')
except ArithmeticError as e:
print ('예외 발생:', e.args[0])





