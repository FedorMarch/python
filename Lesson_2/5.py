rate = [7, 5, 3, 3, 2]
print(rate)
rate.append(int(input('Добавь значение в рейтинг')))
rate = sorted(rate)
rate.reverse()
print(rate)