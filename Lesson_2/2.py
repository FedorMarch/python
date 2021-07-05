data = input('Введите несколько элементов').split()
i = 0
while i < len(data):
    if len(data) % 2 == 0 or i + 1 != len(data):
        var_1, var_2 = data[i], data[i + 1]
        var_1, var_2 = var_2, var_1
        data[i], data[i + 1] = var_1, var_2
    i += 2
print(data)
