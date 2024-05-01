from Classes.base import Food
from datetime import datetime
class Product(Food):
    def __init__(self, name, quantity, expiration_date):
        super().__init__(name)
        self._quantity = quantity
        self._expiration_date = expiration_date

    def __str__(self):
        return f"{self.name} (x{self.quantity})"

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value

    @property
    def expiration_date(self):
        return self._expiration_date

    def check_expiration(self):
        return self._expiration_date > datetime.now()

    def is_expired(self):
        return self._expiration_date < datetime.now().date()