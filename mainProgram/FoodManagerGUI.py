import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QLineEdit, QPushButton, QComboBox, QLabel, QMessageBox
from datetime import datetime, timedelta

import Classes.Refrigerator, Classes.Food,Classes.PerishableProduct,Classes.Product,Classes.Statistics
from Classes import *


class FoodManagerGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Food Manager")
        self.setGeometry(100, 100, 400, 300)

        self.refrigerator = Classes.Fridge.Refrigerator()
        self.statistics = Classes.Analyzer.Statistics(self.refrigerator)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.main_layout = QVBoxLayout()
        self.central_widget.setLayout(self.main_layout)

        self.add_product_layout = QHBoxLayout()
        self.add_dish_layout = QHBoxLayout()

        # Add Product
        self.product_name_label = QLabel("Product Name:")
        self.product_name_input = QLineEdit()
        self.product_quantity_label = QLabel("Quantity:")
        self.product_quantity_input = QLineEdit()
        self.product_expiration_label = QLabel("Expiration Date:")
        self.product_expiration_input = QLineEdit()
        self.add_product_button = QPushButton("Add Product")
        self.add_product_button.clicked.connect(self.add_product)

        self.add_product_layout.addWidget(self.product_name_label)
        self.add_product_layout.addWidget(self.product_name_input)
        self.add_product_layout.addWidget(self.product_quantity_label)
        self.add_product_layout.addWidget(self.product_quantity_input)
        self.add_product_layout.addWidget(self.product_expiration_label)
        self.add_product_layout.addWidget(self.product_expiration_input)
        self.add_product_layout.addWidget(self.add_product_button)

        # Add Dish
        self.dish_name_label = QLabel("Dish Name:")
        self.dish_name_input = QLineEdit()
        self.dish_ingredients_label = QLabel("Ingredients:")
        self.dish_ingredients_input = QComboBox()
        for food in self.refrigerator._foods:
            self.dish_ingredients_input.addItem(food.name)
        self.add_dish_button = QPushButton("Add Dish")
        self.add_dish_button.clicked.connect(self.add_dish)

        self.add_dish_layout.addWidget(self.dish_name_label)
        self.add_dish_layout.addWidget(self.dish_name_input)
        self.add_dish_layout.addWidget(self.dish_ingredients_label)
        self.add_dish_layout.addWidget(self.dish_ingredients_input)
        self.add_dish_layout.addWidget(self.add_dish_button)

        self.main_layout.addLayout(self.add_product_layout)
        self.main_layout.addLayout(self.add_dish_layout)

    def add_product(self):
        product_name = self.product_name_input.text()
        product_quantity = int(self.product_quantity_input.text())
        product_expiration_date = datetime.strptime(self.product_expiration_input.text(), "%Y-%m-%d")
        new_product =Classes.PerishableProduct(product_name, product_quantity, product_expiration_date)
        self.refrigerator.add_food(new_product)
        self.product_name_input.clear()
        self.product_quantity_input.clear()
        self.product_expiration_input.clear()
        QMessageBox.information(self, "Success", f"{product_name} has been added to the refrigerator.")

    def add_dish(self):
        dish_name = self.dish_name_input.text()
        selected_ingredients = [self.refrigerator._foods[i] for i in range(self.dish_ingredients_input.count()) if self.dish_ingredients_input.itemText(i) in [food.name for food in self.refrigerator._foods]]
        new_dish =Classes.Dish(dish_name, selected_ingredients)
        self.refrigerator.add_food(new_dish)
        self.dish_name_input.clear()
        self.dish_ingredients_input.clear()
        QMessageBox.information(self, "Success", f"{dish_name} has been added to the refrigerator.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    food_manager_gui = FoodManagerGUI()
    food_manager_gui.show()
    sys.exit(app.exec_())