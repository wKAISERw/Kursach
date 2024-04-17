from datetime import datetime, timedelta
from collections import Counter
import Food
class Dish(Food):
    def __init__(self, name, ingredients):
        super().__init__(name)
        self._ingredients = ingredients

    @property
    def ingredients(self):
        return self._ingredients