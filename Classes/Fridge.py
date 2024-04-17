from datetime import datetime, timedelta
from collections import Counter
import Product
class Refrigerator:
    def __init__(self):
        self._foods = []

    def add_food(self, food):
        self._foods.append(food)

    def remove_food(self, food):
        self._foods.remove(food)

    def check_availability(self, food_name):
        for food in self._foods:
            if food.name == food_name:
                if isinstance(food, Product):
                    return food.quantity > 0
                else:
                    return True
        return False