from datetime import datetime, timedelta
from collections import Counter
from Classes.base import Food
from datetime import datetime, timedelta
from collections import Counter
from Classes.base import Food

class Dish(Food):
    def __init__(self, name):
        super().__init__(name)
        self._products = []

    def add_product(self, product):
        self._products.append(product)

    def remove_product(self, product):
        self._products.remove(product)
        product.quantity += 1

    @property
    def products(self):
        return self._products

    @products.setter
    def products(self, value):
        self._products = value