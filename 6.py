a = float(input('Введите результат первого дня: '))
b = int(input('Введите цель: '))
day = 1
while a < b:
    a = a * 1.1
    day = day +1
print(f"На {day}-й день спортсмен достиг результата — не менее {b} км.")