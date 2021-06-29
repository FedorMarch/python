sec = int(input('Введите время в секундах: '))
hours = sec // 3600
minutes = (sec % 3600) // 60
seconds = (sec % 3600) % 60
print(f"Точное время {hours}:{minutes}:{seconds}")
