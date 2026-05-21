fish_cutlet = {'пангасиус-минтай':5000, 'филе куринное':5000, 'сало':2500, 'лук':2500, 'хлеб':700, 'соль':100}

while True:
    n = float(input('Введите сколько кг рыбы у вас в наличии для замеса - ')) / 5
    total_weight = 0
    for i in fish_cutlet:
            weight_i = int(fish_cutlet[i] * n)
            total_weight += weight_i
            print(i, '-', str(weight_i) + 'г')
    print()
    print('Общий вес - ', str(total_weight) + 'г')
    print()