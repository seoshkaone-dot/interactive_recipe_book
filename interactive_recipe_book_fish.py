fish_cutlet = {'пангасиус':2500, 'минтай':2500, 'филе куринное':5000, 'сало':2500, 'лук':2500, 'хлеб':1050, 'соль':100}

while True:
    n_p = float(input('Введите сколько кг пангасиус у вас в наличии для замеса - '))
    n_m = float(input('Введите сколько кг минтай у вас в наличии для замеса - '))
    n = (n_p / 2.5 + n_m / 2.5) / 2
    n_p = int(n_p * 1000)
    n_m = int(n_m * 1000)
    total_weight = n_p + n_m
    print('пангасиус -', str(n_p) + 'г')
    print('минтай -', str(n_m) + 'г')
    for i in fish_cutlet:
            if i != 'пангасиус' and i != 'минтай':
                weight_i = int(fish_cutlet[i] * n)
                total_weight += weight_i
                print(i, '-', str(weight_i) + 'г')
    print()
    print('Общий вес - ', str(total_weight) + 'г')
    print()