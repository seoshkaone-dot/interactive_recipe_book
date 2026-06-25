from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner

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

        button = Button(text='Кнопка')
        button.bind(on_press=self.show_recipes)
        layout.add_widget(button)

        self.recipe_label = Label(text='Нажмите кнопку для показа рецептов')
        layout.add_widget(self.recipe_label)

        return layout
    
    def on_recipe_select(self, spinner, text):
        ingredients = self.manager.get_ingredients(text)
        self.ingredient_spinner.values = ingredients
        if ingredients:
            self.ingredient_spinner.text = ingredients[0]

    def show_recipes(self, *args):
        recipe_names = self.manager.get_recipe_names()
        self.recipe_label.text = '\n'.join(recipe_names)

if __name__ == '__main__':
    RecipeBookApp().run()
