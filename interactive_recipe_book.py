while True:
    print('Какой рецепт вы хотите посчитать?')
    print('1 - люля-кебаб', '2 - котлеты куринные', '3 - шницель', sep='\n')
    index_recipe = int(input('Введите индекс рецепта - '))
    n = float(input('Введите сколько кг мяса у вас в наличии для замеса - ')) / 10
    total_weight = 0
    if index_recipe == 1:
        kebab = {'филе куринное':10000, 'сало':3000, 'лук':3000, 'хлеб':350, 'соль':100}
        for i in kebab:
            weight_i = int(kebab[i] * n)
            total_weight += weight_i
            print(i, '-', str(weight_i) + 'г')
    elif index_recipe == 2:
        chicken_cutlet = {'филе куриное':10000, 'сало':3000, 'лук':1500, 'хлеб':1400, 'соль':100, 'вода':1200}
        for i in chicken_cutlet:
            weight_i = int(chicken_cutlet[i] * n)
            total_weight += weight_i
            print(i, '-', str(int(weight_i)) + 'г')
    elif index_recipe == 3:
        schnitzel = {'свинина':3000, 'филе куриное':7000, 'сало':3000, 'чеснок':50, 'лук':1500, 'хлеб':1400, 'соль':100, 'вода':700}
        for i in schnitzel:
            weight_i = int(schnitzel[i] * n)
            total_weight += weight_i
            print(i, '-', str(int(weight_i)) + 'г')
    else:
        print()
        print('По-моему вы что-то перепутали, проверьте индекс.')
        print()
        continue
    print('Общий вес - ', str(total_weight) + 'г')
    print()
