from datetime import datetime, timedelta
from collections import Counter

class Refrigerator:
    def __init__(self):
        self._foods = []

    def add_food(self, food):
        self._foods.append(food)

    def remove_food(self, food):
        self._foods.remove(food)