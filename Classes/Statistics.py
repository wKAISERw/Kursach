from datetime import datetime, timedelta
from collections import Counter
import Product, Dish

class Statistics:
    def __init__(self, refrigerator):
        self._refrigerator = refrigerator

    def analyze_foods(self):
        product_counts = Counter(food.name for food in self._refrigerator._foods if isinstance(food, Product))
        low_stock_products = [name for name, count in product_counts.items() if count <= 3]
        expired_foods = [food for food in self._refrigerator._foods if
                         isinstance(food, Product) and not food.check_expiration()]
        return len(self._refrigerator._foods), len(
            [food for food in self._refrigerator._foods if isinstance(food, Dish)]), low_stock_products, expired_foods

    def recommend_purchases(self):
        total_foods, total_dishes, low_stock_products, expired_foods = self.analyze_foods()
        recommendations = []
        recommendations.append(f"Total Foods: {total_foods}")
        recommendations.append(f"Total Dishes: {total_dishes}")
        if low_stock_products:
            recommendations.append("You should buy more of the following products:")
            for product_name in low_stock_products:
                recommendations.append(f"- {product_name}")
        if expired_foods:
            recommendations.append("The following products have expired or are about to expire:")
            for product in expired_foods:
                recommendations.append(
                    f"- {product.name} (Expiration date: {product.expiration_date.strftime('%Y-%m-%d')})")
        return recommendations

    def analyze_low_stock(self):
        low_stock_products = []
        for food in self._refrigerator._foods:
            if isinstance(food, Product) and food.quantity <= 5:
                low_stock_products.append(f"{product.name} (x{quantity})")

        return low_stock_products
