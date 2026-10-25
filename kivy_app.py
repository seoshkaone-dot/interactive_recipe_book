import os

from kivy.app import App
from kivy.graphics import Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup

from recipe_manager import RecipeManager


class RecipeBookApp(App):
    def _update_background(self, instance, value):
        if hasattr(self, 'background'):
            self.background.pos = instance.pos
            self.background.size = instance.size

    def build(self):
        self.manager = RecipeManager()

        root = FloatLayout()
        bg_path = os.path.join(os.path.dirname(__file__), 'b5453e42-709e-468f-b4e8-41a1f6bfd94b.png')
        with root.canvas.before:
            self.background = Rectangle(source=bg_path, pos=root.pos, size=root.size)
        root.bind(size=self._update_background, pos=self._update_background)

        layout = BoxLayout(orientation='vertical', padding=16, spacing=16)
        layout.add_widget(Label(text='Интерактивная книга рецептов', color=(0, 0, 0, 1), font_size='24sp'))

        self.recipe_spinner = Spinner(
            text='Выберите рецепт',
            values=self.manager.get_recipe_names()
        )
        self.recipe_spinner.bind(text=self.on_recipe_select)
        layout.add_widget(self.recipe_spinner)

        recipe_actions = BoxLayout(size_hint_y=None, height=44, spacing=8)
        add_button = Button(text='Добавить рецепт')
        add_button.bind(on_press=self.show_add_recipe)
        recipe_actions.add_widget(add_button)

        delete_button = Button(text='Удалить рецепт')
        delete_button.bind(on_press=self.show_delete_recipe)
        recipe_actions.add_widget(delete_button)
        layout.add_widget(recipe_actions)

        self.ingredient_spinner = Spinner(
            text='Выберите ингредиент',
            values=[]
        )
        layout.add_widget(self.ingredient_spinner)

        self.kg_input = TextInput(
            hint_text='Введите количество\n(в граммах)',
            input_filter='float',
            multiline=False
        )
        layout.add_widget(self.kg_input)

        button = Button(text='Рассчитать')
        button.bind(on_press=self.calculate_recipe)
        layout.add_widget(button)

        self.recipe_label = Label(text='Нажмите кнопку для показа рецептов', color=(0, 0, 0, 1), size_hint=(1, 2))
        layout.add_widget(self.recipe_label)

        root.add_widget(layout)
        return root
    
    def show_add_recipe(self, *args):
        content = BoxLayout(orientation='vertical', spacing=8, padding=12)
        recipe_input = TextInput(
            hint_text='Название рецепта',
            multiline=False,
            size_hint_y=None,
            height=44
        )
        ingredients_input = TextInput(
            hint_text='Ингредиенты, по одному на строке:\nФиле куриное: 1000',
            multiline=True
        )
        status_label = Label(text='', size_hint_y=None, height=32)
        actions = BoxLayout(size_hint_y=None, height=44, spacing=8)
        popup = Popup(
            title='Новый рецепт',
            content=content,
            size_hint=(0.9, 0.8)
        )

        def save_recipe(*_):
            try:
                ingredients = {}
                for line in ingredients_input.text.splitlines():
                    if not line.strip():
                        continue
                    ingredient, separator, amount = line.partition(':')
                    if not separator:
                        raise ValueError('Для ингредиента укажите количество через двоеточие')
                    ingredient = ingredient.strip()
                    if ingredient in ingredients:
                        raise ValueError(f'Ингредиент «{ingredient}» указан несколько раз')
                    try:
                        ingredients[ingredient] = float(amount.strip())
                    except ValueError as error:
                        raise ValueError(f'Укажите число граммов для «{ingredient}»') from error

                self.manager.add_recipe(recipe_input.text, ingredients)
            except (ValueError, OSError) as error:
                status_label.text = f'Ошибка: {error}'
                return

            self._refresh_recipe_list(recipe_input.text)
            popup.dismiss()

        save_button = Button(text='Сохранить')
        save_button.bind(on_press=save_recipe)
        actions.add_widget(save_button)
        cancel_button = Button(text='Отмена')
        cancel_button.bind(on_press=popup.dismiss)
        actions.add_widget(cancel_button)

        content.add_widget(recipe_input)
        content.add_widget(ingredients_input)
        content.add_widget(status_label)
        content.add_widget(actions)
        popup.open()

    def show_delete_recipe(self, *args):
        recipe_name = self.recipe_spinner.text
        if recipe_name not in self.manager.get_recipe_names():
            self._show_message('Выберите рецепт для удаления')
            return

        content = BoxLayout(orientation='vertical', spacing=12, padding=12)
        content.add_widget(Label(text=f'Удалить рецепт «{recipe_name}»?'))
        actions = BoxLayout(size_hint_y=None, height=44, spacing=8)
        popup = Popup(
            title='Подтверждение удаления',
            content=content,
            size_hint=(0.8, 0.35)
        )

        def delete_recipe(*_):
            try:
                self.manager.delete_recipe(recipe_name)
            except (ValueError, OSError) as error:
                self._show_message(f'Не удалось удалить рецепт: {error}')
                popup.dismiss()
                return

            recipe_names = self.manager.get_recipe_names()
            self._refresh_recipe_list(recipe_names[0] if recipe_names else None)
            popup.dismiss()

        confirm_button = Button(text='Удалить')
        confirm_button.bind(on_press=delete_recipe)
        actions.add_widget(confirm_button)
        cancel_button = Button(text='Отмена')
        cancel_button.bind(on_press=popup.dismiss)
        actions.add_widget(cancel_button)
        content.add_widget(actions)
        popup.open()

    def _refresh_recipe_list(self, selected_recipe=None):
        recipe_names = self.manager.get_recipe_names()
        self.recipe_spinner.values = recipe_names
        if selected_recipe in recipe_names:
            self.recipe_spinner.text = selected_recipe
        elif recipe_names:
            self.recipe_spinner.text = recipe_names[0]
        else:
            self.recipe_spinner.text = 'Выберите рецепт'
            self.ingredient_spinner.values = []
            self.ingredient_spinner.text = 'Выберите ингредиент'
        self.recipe_label.text = 'Нажмите кнопку для показа рецептов'

    def _show_message(self, message):
        Popup(
            title='Сообщение',
            content=Label(text=message),
            size_hint=(0.8, 0.3)
        ).open()

    def on_recipe_select(self, spinner, text):
        if text not in self.manager.get_recipe_names():
            self.ingredient_spinner.values = []
            self.ingredient_spinner.text = 'Выберите ингредиент'
            return
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
