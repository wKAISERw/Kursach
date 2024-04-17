import Product
from datetime import datetime, timedelta
from collections import Counter
class PerishableProduct(Product):
    def __init__(self, name, quantity, expiration_date):
        super().__init__(name, quantity)
        self._expiration_date = expiration_date
    @property
    def expiration_date(self):
        return self._expiration_date

    def check_expiration(self):
        return self._expiration_date > datetime.now()
