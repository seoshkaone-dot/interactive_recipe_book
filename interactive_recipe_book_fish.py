fish_cutlet = {'пангасиус':2500, 'минтай':2500, 'филе куринное':5000, 'сало':2500, 'лук':2500, 'хлеб':1050, 'соль':100}
liezon = {'соль':35, 'вода':3800, 'мука':2340}

while True:
    print('Какой рецепт вы хотите посчитать?')
    print('1 - льезон, 2 - рыбные котлеты', sep='\n')
    choice = int(input('Введите цифру - '))
    if choice == 1:
        n = float(input('Введите сколько отбивных у вас в наличии - ')) / 150
        total_weight = 0
        for i in liezon:
            weight_i = int(liezon[i] * n)
            total_weight += weight_i
            if i == 'вода':
                print(i, '-', str(weight_i - 800) + 'г')
                print('молоко - 800г')
            else:
                print(i, '-', str(weight_i) + 'г')
        print()
        print('Общий вес - ', str(int(total_weight)) + 'г')
        print()
    else:
        n_p = float(input('Введите сколько кг пангасиус у вас в наличии для замеса - '))
        n_m = float(input('Введите сколько кг минтай у вас в наличии для замеса - '))
        n = (n_p / 2.5 + n_m / 2.5) / 2
        n_p *= 1000
        n_m *= 1000
        if n >= 2:
            n /= 2
            n_p /= 2
            n_m /= 2
            print()
            print('Слишком много, поделенно на два замеса')
        total_weight = n_p + n_m
        print()
        print('пангасиус -', str(int(n_p)) + 'г')
        print('минтай -', str(int(n_m)) + 'г')
        for i in fish_cutlet:
            if i != 'пангасиус' and i != 'минтай':
                weight_i = int(fish_cutlet[i] * n)
                total_weight += weight_i
                print(i, '-', str(weight_i) + 'г')
        print()
        print('Общий вес - ', str(int(total_weight)) + 'г')
        print()