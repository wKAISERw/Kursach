from datetime import datetime, timedelta
from collections import Counter
from Classes.base import Food
class Dish(Food):
    def __init__(self, name):
        super().__init__(name)
        self._ingredients = []

    def add_ingredient(self, ingredient):
        self._ingredients.append(ingredient)

    def remove_ingredient(self, ingredient):
        self._ingredients.remove(ingredient)

    @property
    def ingredients(self):
        return self._ingredients

    @ingredients.setter
    def ingredients(self, value):
        self._ingredients = value