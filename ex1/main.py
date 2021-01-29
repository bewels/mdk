import math
a = 5
b = 10
b = (a + b) - b
a = (a + b)
print(b, a)

num = int(input())
a = 0
num = str(num)
for i in num:
    i = int(i)
    a += i
print(a)


a, b, c = map(int, input('Введите а Ь с ').split())

def aaa(a, b, c):
    D = b ** 2 - 4 * a * c
    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        return x1, x2
    elif D == 0:
        x = (-b) / (2 * a)
        return x
    else:
        return 'D < 0'

print(aaa(a, b, c))



