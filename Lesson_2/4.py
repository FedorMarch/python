text_list = input('Введите несколько слов через пробел').split()
for ind, el in enumerate(text_list, 1):
    print(ind, el[:10])
