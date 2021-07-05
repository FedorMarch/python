i = 1
spisok = []
name_list = []
price_list = []
quant_list = []
ed_list = []
analysis = {'name':name_list, 'price':price_list, 'quant':quant_list, 'ed':ed_list}
while True:
    spisok.append((i, {'name':input('Введите имя товара: '), 'price':input('Введите цену товара: '), 'quant':input('Введите кол-во товара: '), 'ed':input('Введите единицы измерения товара: '), }))
    answer = input('Введите Done, если список закончен. Любой другой символ, если нет')
    if answer == 'Done':
        break
for el in spisok:
    name_list.append(el[1]['name'])
    price_list.append(el[1]['price'])
    quant_list.append(el[1]['quant'])
    ed_list.append(el[1]['ed'])
print(analysis)