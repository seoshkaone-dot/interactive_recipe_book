kebab = {'мясо':10000, 'сало':3000, 'лук':3000, 'хлеб':350, 'соль':100}
chicken_cutlet = {'мясо':10000, 'сало':3000, 'лук':1500, 'хлеб':1400, 'соль':100, 'вода':1200}

while True:
    print('Какой рецепт вы хотите посчитать?')
    print('1 - люля-кебаб', '2 - котлеты куринные', sep='\n')
    index_recipe = int(input('Введите индекс рецепта - '))
    if index_recipe == 1:
        n = float(input('Введите сколько кг мяса у вас в наличии для замеса - ')) / 10
        for i in kebab:
            print(i, '-', str(int(kebab[i] * n)) + 'г')
    elif index_recipe == 2:
        n = float(input('Введите сколько кг мяса у вас в наличии для замеса - ')) / 10
        for i in chicken_cutlet:
            print(i, '-', str(int(chicken_cutlet[i] * n)) + 'г')
    else:
        print('По-моему вы что-то перепутали')
    print()