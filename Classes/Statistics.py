from datetime import datetime, date

from Classes.Product import Product
from Classes.Dish import Dish

class Statistics:
    def __init__(self, refrigerator):
        self._refrigerator = refrigerator

    def get_total_counts(self):
        total_foods = len(self._refrigerator._foods)
        total_products = len([food for food in self._refrigerator._foods if isinstance(food, Product)])
        total_dishes = len([food for food in self._refrigerator._foods if isinstance(food, Dish)])
        return total_foods, total_products, total_dishes

    def analyze_low_stock(self):
        low_stock_products = []
        for food in self._refrigerator._foods:
            if isinstance(food, Product) and food.quantity <= 5:
                low_stock_products.append(f"{food.name} (x{food.quantity})")

        return low_stock_products

    def get_expiring_products(self, days=7):
        expiring_products = []
        today = date.today()
        for food in self._refrigerator._foods:
            if isinstance(food, Product) and isinstance(food.expiration_date, date):
                expiration_datetime = datetime.combine(food.expiration_date, datetime.min.time())
                days_until_expiration = (expiration_datetime - datetime.combine(today, datetime.min.time())).days
                if 0 < days_until_expiration <= days:
                    expiring_products.append(food)
        return expiring_products

