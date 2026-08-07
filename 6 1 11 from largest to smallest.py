# Напишите программу, которая упорядочивает три числа от большего к меньшему.

a, b, c = int(input()), int(input()), int(input())

mx = max(a, b, c)
mn = min(a, b, c)

print(mx)
print(a + b + c - mx - mn)
print(mn)
