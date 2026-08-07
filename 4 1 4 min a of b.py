# определяет наименьшее из двух чисел

a = int(input())
b = int(input())
if a < b:
    print(a)
else:
    print(b)

print("Наименьшее число =", min(a, b))
print("Наибольшее число =", max(a, b))
