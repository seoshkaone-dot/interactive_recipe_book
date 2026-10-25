import json
import math


class RecipeManager:
    def __init__(self, path='recipes.json'):
        self.path = path
        self.recipes = self.load_recipes(path)
    
    def load_recipes(self, path):
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def _save_recipes(self, recipes):
        with open(self.path, 'w', encoding='utf-8') as f:
            json.dump(recipes, f, ensure_ascii=False, indent=2)
            f.write('\n')
    
    def get_recipe_names(self):
        return list(self.recipes)
    
    def get_ingredients(self, recipe_name):
        return list(self.recipes[recipe_name])

    def add_recipe(self, recipe_name, ingredients):
        recipe_name = recipe_name.strip()
        if not recipe_name:
            raise ValueError('Введите название рецепта')
        if recipe_name in self.recipes:
            raise ValueError('Рецепт с таким названием уже существует')
        if not ingredients:
            raise ValueError('Добавьте хотя бы один ингредиент')

        normalized_ingredients = {}
        for ingredient, weight in ingredients.items():
            ingredient = ingredient.strip()
            if not ingredient:
                raise ValueError('Название ингредиента не может быть пустым')
            if ingredient in normalized_ingredients:
                raise ValueError(f'Ингредиент «{ingredient}» указан несколько раз')
            if isinstance(weight, bool) or not isinstance(weight, (int, float)):
                raise ValueError(f'Количество ингредиента «{ingredient}» должно быть числом')
            if not math.isfinite(weight) or weight <= 0:
                raise ValueError(f'Количество ингредиента «{ingredient}» должно быть больше 0')
            normalized_ingredients[ingredient] = weight

        updated_recipes = dict(self.recipes)
        updated_recipes[recipe_name] = normalized_ingredients
        self._save_recipes(updated_recipes)
        self.recipes = updated_recipes

    def delete_recipe(self, recipe_name):
        if recipe_name not in self.recipes:
            raise ValueError('Выберите существующий рецепт')

        updated_recipes = dict(self.recipes)
        del updated_recipes[recipe_name]
        self._save_recipes(updated_recipes)
        self.recipes = updated_recipes

    def calculate(self, recipe_name, ingredient, target_kg):
        recipe = self.recipes[recipe_name]
        result = {}
        total_weight = 0
        scale = target_kg / (recipe[ingredient])
        for i in recipe:
            weight_i = int(recipe[i] * scale)
            total_weight += weight_i
            result[i] = weight_i
        return result, total_weight
