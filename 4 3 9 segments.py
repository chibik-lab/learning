# На числовой прямой даны два отрезка: [a1; b1][a1​;b1​] и [a2; b2][a2​;b2​]. Напишите программу, которая находит их пересечение.
# Пересечением двух отрезков может быть: отрезок, точка, пустое множество:
# На вход программе подаются четыре целых числа a1, b1, a2, b2, каждое на отдельной строке. Гарантируется, что a1<b1  и a2<b2  ​​.

a = int(input())
a1 = int(input())
b = int(input())
b1 = int(input())

if a > b:
    left = a
else:
    left = b

if b1 > a1:
    right = a1
else:
    right = b1


if left < right:
    print(left, right)  # Получился отрезок
elif left == right:
    print(left)  # Получилась точка
else:
    print("пустое множество")

"""
if a1 >=b>a and b1> a1>b: #наложение отрезков
    print(b, a1)
elif a >= b and a1<=b1: #отрезок AA1 внутри отрезка BB1 
    print(a, a1)
elif a1==b:             #точки совпадают
    print(b) 
elif a==b1:             #точки совпадают
    print(a) 
elif a1 >= b >= a and a1>=b1>a: #отрезок BB1 внутри отрезка AA1 
    print(b, b1)
elif b1 >=a>b and a1> b1>a:     #наложение отрезков
    print(a, b1)

else:
    print("пустое множество")
    
"""
