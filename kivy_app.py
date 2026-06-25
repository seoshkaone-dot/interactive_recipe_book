from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput

from recipe_manager import RecipeManager


class RecipeBookApp(App):
    def build(self):
        self.manager = RecipeManager()

        layout = BoxLayout(orientation='vertical', padding=16, spacing=16)
        layout.add_widget(Label(text='Интерактивная книга рецептов', font_size='24sp'))

        self.recipe_spinner = Spinner(
            text='Выберите рецепт',
            values=self.manager.get_recipe_names()
        )
        self.recipe_spinner.bind(text=self.on_recipe_select)
        layout.add_widget(self.recipe_spinner)

        self.ingredient_spinner = Spinner(
            text='Выберите ингредиент',
            values=[]
        )
        layout.add_widget(self.ingredient_spinner)

        self.kg_input = TextInput(
            hint_text='Введите количество (кг)',
            input_filter='float',
            multiline=False
        )
        layout.add_widget(self.kg_input)

        button = Button(text='Рассчитать')
        button.bind(on_press=self.calculate_recipe)
        layout.add_widget(button)

        self.recipe_label = Label(text='Нажмите кнопку для показа рецептов')
        layout.add_widget(self.recipe_label)

        return layout
    
    def on_recipe_select(self, spinner, text):
        ingredients = self.manager.get_ingredients(text)
        self.ingredient_spinner.values = ingredients
        if ingredients:
            self.ingredient_spinner.text = ingredients[0]

    def calculate_recipe(self, *args):
        try:
            recipe_name = self.recipe_spinner.text
            ingredient = self.ingredient_spinner.text
            target_kg = float(self.kg_input.text)

            if target_kg <= 0:
                self.recipe_label.text = 'Ошибка! Число должно быть больше 0'
                return
            result, total_weight = self.manager.calculate(recipe_name, ingredient, target_kg)

            text_result = f'Расчет для {recipe_name}:\n'
            for ing, weight in result.items():
                text_result += f'{ing}: {weight} г\n'
            text_result += f'\nОбщий вес: {total_weight} г'

            self.recipe_label.text = text_result
        except Exception as e:
            self.recipe_label.text = f'Ошибка: {str(e)}'

if __name__ == '__main__':
    RecipeBookApp().run()
