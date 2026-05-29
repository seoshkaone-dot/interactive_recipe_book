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

def calculate_recipe(recipe, ingredient, target_kg):
    result = {}
    total_weight = 0
    scale = target_kg / (recipe[ingredient] / 1000)
    for i in recipe:
        weight_i = int(recipe[i] * scale)
        total_weight += weight_i
        result[i] = weight_i
    return result, total_weight

while True:
    print('Рецепты:')
    print(*recipes, sep='\n')
    recipe_name = input('Введите наименование рецепта - ')
    print()
    recipe = recipes.get(recipe_name, 'Ошибка! Такого рецепта нет')
    if recipe == 'Ошибка! Такого рецепта нет':
        print(recipe)
        print()
        continue
    print('Ингредиенты:')
    print(*recipe.keys(), sep='\n')
    while True:
        ingredient = input('Введите наименование ингредиента - ')
        if ingredient not in recipe:
            print()
            print('Ошибка! Такого ингредиента нет')
            print()
            continue
        else:
            break
    while True:
        try:
            target_kg = float(input('Введите сколько кг - '))
            if target_kg <= 0:
                print()
                print('Ошибка! Число должно быть больше 0')
                print()
                continue
            break
        except ValueError:
            print('Ошибка! Введите число (например: 2.5)')
    print()
    print('Готовый расчет:')
    result, total_weight = calculate_recipe(recipe, ingredient, target_kg)
    for ing, w in result.items():
        print(f'{ing} - {w} г')
    print('Общий вес -', f'{total_weight} г')
    print()
