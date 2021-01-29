# print('Приветсвие!')
# a = int(input())
# b = int(input())
# i = 0
# x = 0
# y = 0
# step = 1
# sumr = 0
# while i == 0:
#     c = 0
#     comand = input('Введите команду ')
#
#     if comand == 'вперед':
#         y += step
#
#     elif comand == 'налево':
#         sumr += 1
#         x, y = y, x
#         step = -1
#
#     elif comand == 'направо':
#         sumr += 1
#         x, y = y, x
#
#     elif comand == 'раз':
#         step = -step
#     elif comand == 'стоп':
#         if sumr % 2 == 0:
#             x, y = y, x
#         print('Ты смог!')
#         print(x, y)
#
#         i += 1
#     else:
#         print('Что то не так!')
#     print(a, b)
#
#
# print('Спасибо за игру!')
#
#




# f = input()
#
# print(f[2])
# print(f[-2])
# print(f[0 : 5])
# print(f[0 : -2])
# print(f[ : : 2])
# print(f[1 :  : 2])
# print(f[ :  : -1])
# print(f[ : : -2])
# print(len(f))





mon = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
res = 0
def day_calendar (d, m, y, c):
    res = (d + ((13 * mon[m - 2] - 1) // 5) + y + (y // 4 + c // 4 - 2 * c + 777)) % 7
    return res
d = int(input())
m = int(input())
y = int(input())
c = y // 100
a = y % 100
print(day_calendar(d, a, m, c))