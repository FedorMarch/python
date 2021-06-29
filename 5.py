vyr = int(input('Введите выручку'))
izd = int(input('Введите издержки'))
itog = vyr - izd
if itog > 0:
    print('Фирма отработала с прибылью, равной', itog)
    print('Рентабельность:', itog / vyr)
    workers = int(input('Введите численность сотрудников'))
    print('Прибыль фирмы в расчете на одного сотрудника:', itog/workers)
else:
    print('Фирма отработала с убытком, равным', itog*(-1))