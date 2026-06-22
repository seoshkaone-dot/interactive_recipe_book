from recipe_manager import RecipeManager


manager = RecipeManager()
recipes = manager.get_recipe_names()

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

while True:
    print('Рецепты:')
    recipe_name = choose_index('Введите индекс рецепта - ', recipes)
    ingredient_names = manager.get_ingredients(recipe_name)
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
    result, total_weight = manager.calculate(recipe_name, ingredient, target_kg)
    for ing, w in result.items():
        print(f'{ing} - {w} г')
    print('Общий вес -', f'{total_weight} г')
    print()
