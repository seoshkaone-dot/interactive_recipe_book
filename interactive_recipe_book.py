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

def choose_index(s, names):
    for index, name in enumerate(names, 1):
        print(index, '-', name)
    while True:
        try:
            index_names = int(input(s))
            if 1 <= index_names <= len(names):
                break
            else:
                print('Ошибка! Такого индекса нет')
                continue
        except ValueError:
            print('Ошибка! Введите число (например: 1)')
    result = names[index_names - 1]
    return result

def calculate_recipe(recipe, ingredient, target_kg):
    result = {}
    total_weight = 0
    print(recipe, ingredient, target_kg)
    scale = target_kg / (recipe[ingredient] / 1000)
    for i in recipe:
        weight_i = int(recipe[i] * scale)
        total_weight += weight_i
        result[i] = weight_i
    return result, total_weight

while True:
    print('Рецепты:')
    recipe_names = list(recipes)
    recipe_name = choose_index('Введите индекс рецепта - ', recipe_names)
    recipe = recipes[recipe_name]
    ingredient_names = list(recipe)
    ingredient = choose_index('Введите индекс ингредиента - ', ingredient_names)
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
