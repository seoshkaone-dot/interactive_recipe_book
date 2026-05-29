recipes = {
    'Люля-кебаб':{'Филе куринное':10000, 'Сало':3000, 'Соль':100, 'Лук':3000, 'Хлеб':350},
    'Котлеты куринные':{'Филе куриное':10000, 'Сало':3000, 'Соль':100, 'Лук':1500, 'Хлеб':1400, 'Вода':1200},
    'Шницель':{'Свинина':3000, 'Филе куриное':7000, 'Сало':3000, 'Соль':100, 'Чеснок':50, 'Лук':3000, 'Хлеб':700},
    'Рыбные котлеты':{'Рыба':5000, 'Филе куринное':5000, 'Сало':2500, 'Соль':100, 'Лук':2500, 'Хлеб':1050},
    'Тефтели':{'Филе куринное':3000, 'Сало':800, 'Соль':30, 'Лук':800, 'Рис':900},
    'Свинно-говяжие люля-кебаб':{'Говядина':3000, 'Свинина':3000, 'Филе куринное':4000, 'Сало':3000, 'Соль':100, 'Лук':3000, 'Хлеб':350},
    'Бифштекс':{'Говядина':6000, 'Филе куринное':4000, 'Сало':3000, 'Соль':100, 'Лук':2000, 'Хлеб':700},
    'Льезон':{'Отбивные':150, 'Соль':35, 'Вода':3800, 'Мука':2340}
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
    recipe_names = list(recipes)
    for index, name in enumerate(recipe_names, 1):
        print(index, '-', name)
    while True:
        index_recipe = int(input('Введите индекс рецепта - '))
        if 1 <= index_recipe <= len(recipe_names):
            break
        else:
            print('Ошибка! Такого индекса нет')
            continue
    recipe_name = recipe_names[index_recipe - 1]
    recipe = recipes[recipe_name]
    ingredient_names = list(recipe)
    for index, name in enumerate(ingredient_names, 1):
        print(index, '-', name)
    while True:
        index_ingredient = int(input('Введите индекс ингредиента - '))
        if 1 <= index_ingredient <= len(ingredient_names):
            break
        else:
            print('Ошибка! Такого индекса нет')
            continue
    ingredient = ingredient_names[index_ingredient - 1]
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
