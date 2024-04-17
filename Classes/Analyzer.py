from datetime import datetime, timedelta
from collections import Counter
import Product
class Statistics:
    def __init__(self, refrigerator):
        self._refrigerator = refrigerator

    def analyze_foods(self):
        product_counts = Counter(food.name for food in self._refrigerator._foods if isinstance(food, Product))
        low_stock_products = [name for name, count in product_counts.items() if count <= 3]
        expired_foods = [food for food in self._refrigerator._foods if not food.check_expiration()]
        return low_stock_products, expired_foods

    def recommend_purchases(self):
        low_stock_products, expired_foods = self.analyze_foods()
        recommendations = []
        if low_stock_products:
            recommendations.append("You should buy more of the following products:")
            for product_name in low_stock_products:
                recommendations.append(f"- {product_name}")
        if expired_foods:
            recommendations.append("The following products have expired or are about to expire:")
            for food in expired_foods:
                if isinstance(food, PerishableProduct):
                    recommendations.append(f"- {food.name} (Expiration date: {food.expiration_date.strftime('%Y-%m-%d')})")
                else:
                    recommendations.append(f"- {food.name}")
        return recommendations