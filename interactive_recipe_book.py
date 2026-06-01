import json


with open('recipes.json', 'r', encoding='utf-8') as f:
    recipes = json.load(f)

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
