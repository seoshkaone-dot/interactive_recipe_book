from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

from recipe_manager import RecipeManager


class RecipeBookApp(App):
    def build(self):
        self.manager = RecipeManager()

        layout = BoxLayout(orientation='vertical', padding=16, spacing=16)
        layout.add_widget(Label(text='Интерактивная книга рецептов', font_size='24sp'))

        button = Button(text='Кнопка')
        button.bind(on_press=self.show_recipes)
        layout.add_widget(button)

        self.recipe_label = Label(text='Нажмите кнопку для показа рецептов')
        layout.add_widget(self.recipe_label)

        return layout
    
    def show_recipes(self, *args):
        recipe_names = self.manager.get_recipe_names()
        self.recipe_label.text = '\n'.join(recipe_names)

if __name__ == '__main__':
    RecipeBookApp().run()
