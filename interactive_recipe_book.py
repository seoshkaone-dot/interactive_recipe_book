kebab = {'мясо':10000, 'сало':3000, 'лук':3000, 'хлеб':350, 'соль':100}
chicken_cutlet = {'мясо':10000, 'сало':3000, 'лук':1500, 'хлеб':1400, 'соль':100, 'вода':1200}

while True:
    print('Какой рецепт вы хотите посчитать?')
    print('1 - люля-кебаб', '2 - котлеты куринные', sep='\n')
    index_recipe = int(input('Введите индекс рецепта - '))
    total_weight = 0
    if index_recipe == 1:
        n = float(input('Введите сколько кг мяса у вас в наличии для замеса - ')) / 10
        for i in kebab:
            weight_i = int(kebab[i] * n)
            total_weight += int(kebab[i] * n)
            print(i, '-', str(weight_i) + 'г')
    elif index_recipe == 2:
        n = float(input('Введите сколько кг мяса у вас в наличии для замеса - ')) / 10
        for i in chicken_cutlet:
            weight_i = int(chicken_cutlet[i] * n)
            total_weight += int(chicken_cutlet[i] * n)
            print(i, '-', str(int(chicken_cutlet[i] * n)) + 'г')
    else:
        print()
        print('По-моему вы что-то перепутали, проверьте индекс.')
        print()
        continue
    print('Общий вес - ', str(total_weight) + 'г')
    print()