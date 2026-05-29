recipes = {
    'Люля-кебаб':{'филе куринное':10000, 'сало':3000, 'соль':100, 'лук':3000, 'хлеб':350},
    'Котлеты куринные':{'филе куриное':10000, 'сало':3000, 'соль':100, 'лук':1500, 'хлеб':1400, 'вода':1200},
    'Шницель':{'свинина':3000, 'филе куриное':7000, 'сало':3000, 'соль':100, 'чеснок':50, 'лук':3000, 'хлеб':700},
    'Рыбные котлеты':{'рыба':5000, 'филе куринное':5000, 'сало':2500, 'соль':100, 'лук':2500, 'хлеб':1050},
    'Тефтели':{'филе куринное':3000, 'сало':800, 'соль':30, 'лук':800, 'рис':900},
    'Свинно-говяжие люля-кебаб':{'говядина':3000, 'свинина':3000, 'филе куринное':4000, 'сало':3000, 'соль':100, 'лук':3000, 'хлеб':350},
    'Бифштекс':{'говядина':6000, 'филе куринное':4000, 'сало':3000, 'соль':100, 'лук':2000, 'хлеб':700},
    'Льезон':{'отбивные':150, 'соль':35, 'вода':3800, 'мука':2340}
}

while True:
    print('Рецепты:')
    print(*recipes, sep='\n')
    recipe_name = input('Введите наименование рецепта - ')
    print()
    recipe = recipes.get(recipe_name, 'Такого рецепта нет')
    if recipe == 'Такого рецепта нет':
        print(recipe)
        print()
        continue
    print('Ингредиенты:')
    print(*recipe.keys(), sep='\n')
    ingredient = input('Введите наименование ингредиента - ')
    target_kg = float(input('Введите сколько кг - '))
    total_weight = 0
    for i in recipe:
        scale = target_kg / (recipe[ingredient] / 1000)
        weight_i = int(recipe[i] * scale)
        total_weight += weight_i
        print(i, '-', str(weight_i) + 'г')
    print('Общий вес - ', str(total_weight) + 'г')
    print()

    '''total_weight = 0
    if index_recipe == 1:
        print(*kebab.keys(), sep='\n')
        s = input('По какому ингредиенту нужно посчитать - ')
        n = float(input('Введите на сколько кг расчитать - ')) / (kebab[s] / 1000)
        for i in kebab:
            weight_i = int(kebab[i] * n)
            total_weight += weight_i
            print(i, '-', str(weight_i) + 'г')
    elif index_recipe == 2:
        print(*chicken_cutlet.keys(), sep='\n')
        s = input('По какому ингредиенту нужно посчитать - ')
        n = float(input('Введите на сколько кг расчитать - ')) / (chicken_cutlet[s] / 1000)
        for i in chicken_cutlet:
            weight_i = int(chicken_cutlet[i] * n)
            total_weight += weight_i
            print(i, '-', str(int(weight_i)) + 'г')
    elif index_recipe == 3:
        print(*schnitzel.keys(), sep='\n')
        s = input('По какому ингредиенту нужно посчитать - ')
        n = float(input('Введите на сколько кг расчитать - ')) / (schnitzel[s] / 1000)
        for i in schnitzel:
            weight_i = int(schnitzel[i] * n)
            total_weight += weight_i
            print(i, '-', str(int(weight_i)) + 'г')
    elif index_recipe == 4:
        print(*fish_cutlet.keys(), sep='\n')
        s = input('По какому ингредиенту нужно посчитать - ')
        n = float(input('Введите на сколько кг расчитать - ')) / (fish_cutlet[s] / 1000)
        for i in fish_cutlet:
            weight_i = int(fish_cutlet[i] * n)
            total_weight += weight_i
            print(i, '-', str(int(weight_i)) + 'г')
    elif index_recipe == 5:
        print(*meatballs.keys(), sep='\n')
        s = input('По какому ингредиенту нужно посчитать - ')
        n = float(input('Введите на сколько кг расчитать - ')) / (meatballs[s] / 1000)
        for i in meatballs:
            weight_i = int(meatballs[i] * n)
            total_weight += weight_i
            print(i, '-', str(int(weight_i)) + 'г')
    elif index_recipe == 6:
        print(*pork_beef_kebabs.keys(), sep='\n')
        s = input('По какому ингредиенту нужно посчитать - ')
        n = float(input('Введите на сколько кг расчитать - ')) / (pork_beef_kebabs[s] / 1000)
        for i in pork_beef_kebabs:
            weight_i = int(pork_beef_kebabs[i] * n)
            total_weight += weight_i
            print(i, '-', str(int(weight_i)) + 'г')
    elif index_recipe == 7:
        print(*steak.keys(), sep='\n')
        s = input('По какому ингредиенту нужно посчитать - ')
        n = float(input('Введите на сколько кг расчитать - ')) / (steak[s] / 1000)
        for i in steak:
            weight_i = int(steak[i] * n)
            total_weight += weight_i
            print(i, '-', str(int(weight_i)) + 'г')
    elif index_recipe == 8:
        n = float(input('Введите сколько отбивных у вас в наличии - ')) / 150
        total_weight = 0
        for i in liezon:
            weight_i = int(liezon[i] * n)
            total_weight += weight_i
            if i == 'вода':
                print('молоко - 800г')
                print(i, '-', str(weight_i - 800) + 'г')
            else:
                print(i, '-', str(weight_i) + 'г')
    else:
        print()
        print('По-моему вы что-то перепутали, проверьте индекс.')
        print()
        continue
    print('Общий вес - ', str(total_weight) + 'г')
    print()
'''