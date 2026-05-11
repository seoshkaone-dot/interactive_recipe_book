kebab = {'мясо':10000, 'сало':3000, 'лук':3000, 'хлеб':350, 'соль':100}

while True:
    print('Какой рецепт вы хотите посчитать?')
    print('1 - люля-кебаб')
    index_recipe = int(input('Введите индекс рецепта - '))
    if index_recipe == 1:
        n = float(input('Введите сколько кг мяса у вас в наличии для замеса - ')) / 10
        for i in kebab:
            print(i, '-', str(int(kebab[i] * n)) + 'г')
    else:
        print('По-моему вы что-то перепутали')
    print()