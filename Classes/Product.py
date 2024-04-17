from datetime import datetime, timedelta
from collections import Counter
import Food
class Product(Food):
    def __init__(self, name, quantity):
        super().__init__(name)
        self._quantity = quantity

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value

