num = int(input('Введите целое положительное число: '))
a = num
b = 0
while a > 10:
    if a % 10 > b:
        b = a % 10
    a = a // 10
if a > b:
    b = a
print (b)