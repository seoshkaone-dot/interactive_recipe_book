import json


class RecipeManager:
    def __init__(self, path='recipes.json'):
        self.recipes = self.load_recipes(path)
    
    def load_recipes(self, path):
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def get_recipe_names(self):
        return list(self.recipes)
    
    def get_ingredients(self, recipe_name):
        return list(self.recipes[recipe_name])

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
