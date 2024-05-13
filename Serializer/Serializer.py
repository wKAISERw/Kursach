import json
from datetime import datetime, date
from Classes.Refrigerator import Refrigerator
from Classes.Product import Product
from Classes.Dish import Dish

class Serializer:
    @staticmethod
    def serialize_product(product):
        return {
            "name": product.name,
            "quantity": product.quantity,
            "expiration_date": product.expiration_date.strftime("%Y-%m-%d")  # Перетворюємо дату в строку
        }

    @staticmethod
    def serialize_dish(dish):
        return {
            "name": dish.name,
            "products": [Serializer.serialize_product(product) for product in dish.products]
        }

    @staticmethod
    def deserialize_product(product_data):
        return Product(
            product_data["name"],
            product_data["quantity"],
            datetime.strptime(product_data["expiration_date"], "%Y-%m-%d")  # Парсимо строку у дату
        )

    @staticmethod
    def deserialize_dish(dish_data, refrigerator):
        dish = Dish(dish_data["name"])
        if "products" in dish_data:
            # Новий формат
            for product_data in dish_data["products"]:
                product = Serializer.deserialize_product(product_data)
                dish.add_product(product)
        else:
            # Старий формат
            for ingredient_name in dish_data["ingredients"]:
                ingredient = next((food for food in refrigerator._foods if
                                   isinstance(food, Product) and food.name == ingredient_name), None)
                if ingredient:
                    dish.add_product(ingredient)
        return dish

    @staticmethod
    def save_data(refrigerator, filename):
        data = {
            "products": [Serializer.serialize_product(product) for product in refrigerator._foods if isinstance(product, Product)],
            "dishes": [Serializer.serialize_dish(dish) for dish in refrigerator._foods if isinstance(dish, Dish)]
        }
        try:
            with open(filename, "w") as file:
                json.dump(data, file, indent=4)
            return True
        except Exception as e:
            print(f"Error saving data: {str(e)}")
            return False

    @staticmethod
    def load_data(refrigerator, filename):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
            refrigerator._foods.clear()
            for product_data in data.get("products", []):
                product = Serializer.deserialize_product(product_data)
                refrigerator.add_food(product)
            for dish_data in data.get("dishes", []):
                dish = Serializer.deserialize_dish(dish_data, refrigerator)
                refrigerator.add_food(dish)
            return True
        except Exception as e:
            print(f"Error loading data: {str(e)}")
            return False
