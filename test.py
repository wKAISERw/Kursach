# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'MainProgram.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again. Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
from collections import Counter
import pickle

class Product:
    def __init__(self, name, quantity, expiration_date):
        self._name = name
        self._quantity = quantity
        self._expiration_date = expiration_date

    @property
    def name(self):
        return self._name

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

class Dish:
    def __init__(self, name, ingredients):
        self._name = name
        self._ingredients = ingredients

    @property
    def name(self):
        return self._name

    @property
    def ingredients(self):
        return self._ingredients

class Refrigerator:
    def __init__(self):
        self._foods = []

    def add_food(self, food):
        self._foods.append(food)

    def remove_food(self, food):
        self._foods.remove(food)

    def check_availability(self, food_name):
        for food in self._foods:
            if food.name == food_name:
                if isinstance(food, Product):
                    return food.quantity > 0
                else:
                    return True
        return False

class Statistics:
    def __init__(self, refrigerator):
        self._refrigerator = refrigerator

    def analyze_foods(self):
        product_counts = Counter(food.name for food in self._refrigerator._foods if isinstance(food, Product))
        low_stock_products = [name for name, count in product_counts.items() if count <= 3]
        expired_foods = [food for food in self._refrigerator._foods if isinstance(food, Product) and not food.check_expiration()]
        return len(self._refrigerator._foods), len([food for food in self._refrigerator._foods if isinstance(food, Dish)]), low_stock_products, expired_foods

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
                recommendations.append(f"- {product.name} (Expiration date: {product.expiration_date.strftime('%Y-%m-%d')})")
        return recommendations

class Ui_MainWindow(object):
    def __init__(self):
        self.refrigerator = Refrigerator()
        self.statistics = Statistics(self.refrigerator)
        self.products_model = QtGui.QStandardItemModel()
        self.dishes_model = QtGui.QStandardItemModel()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1332, 726)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listViewProducts = QtWidgets.QListView(self.centralwidget)
        self.listViewProducts.setGeometry(QtCore.QRect(40, 70, 581, 441))
        self.listViewProducts.setObjectName("listViewProducts")
        self.listViewProducts.setModel(self.products_model)
        self.pushButtonAddItem = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonAddItem.setGeometry(QtCore.QRect(40, 520, 371, 51))
        self.pushButtonAddItem.setStyleSheet("font-size: 16pt;")
        self.pushButtonAddItem.setObjectName("pushButtonAddItem")
        self.pushButtonAddItem.setText("Add Item")
        self.pushButtonAddItem.clicked.connect(self.add_item)
        self.pushButtonSave = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSave.setGeometry(QtCore.QRect(520, 10, 93, 28))
        self.pushButtonSave.setObjectName("pushButtonSave")

        self.pushButtonLoad = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonLoad.setGeometry(QtCore.QRect(620, 10, 93, 28))
        self.pushButtonLoad.setObjectName("pushButtonLoad")


        self.pushButtonEdit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonEdit.setGeometry(QtCore.QRect(720, 10, 93, 28))
        self.pushButtonEdit.setObjectName("pushButtonEdit")
        self.pushButtonEdit.clicked.connect(self.edit_product_or_dish)
        self.pushButtonRemoveProduct = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonRemoveProduct.setGeometry(QtCore.QRect(40, 520, 181, 51))
        self.pushButtonRemoveProduct.setStyleSheet("font-size: 16pt;\n"
                                                  "")
        self.pushButtonRemoveProduct.setObjectName("pushButtonRemoveProduct")
        self.pushButtonRemoveProduct.clicked.connect(self.remove_product)
        self.pushButtonRemoveDish = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonRemoveDish.setGeometry(QtCore.QRect(690, 160, 181, 51))
        self.pushButtonRemoveDish.setStyleSheet("font-size: 16pt;\n"
                                               "")
        self.pushButtonRemoveDish.setObjectName("pushButtonRemoveDish")
        self.pushButtonRemoveDish.clicked.connect(self.remove_dish)
        self.labelStatistic = QtWidgets.QLabel(self.centralwidget)
        self.labelStatistic.setGeometry(QtCore.QRect(970, 70, 351, 211))
        self.labelStatistic.setObjectName("labelStatistic")
        self.pushButtonShowStatistics = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonShowStatistics.setGeometry(QtCore.QRect(970, 100, 351, 51))
        self.pushButtonShowStatistics.setStyleSheet("font-size: 16pt;\n"
                                                   "")
        self.pushButtonShowStatistics.setObjectName("pushButtonShowStatistics")
        self.pushButtonShowStatistics.clicked.connect(self.show_statistics)
        self.listViewDish = QtWidgets.QListView(self.centralwidget)
        self.listViewDish.setGeometry(QtCore.QRect(690, 230, 621, 461))
        self.listViewDish.setObjectName("listViewDish")
        self.listViewDish.setModel(self.dishes_model)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.pushButtonSave.setText(_translate("MainWindow", "Зберегти"))
        self.pushButtonLoad.setText(_translate("MainWindow", "Завантажити"))

        self.pushButtonEdit.setText(_translate("MainWindow", "Редагувати"))
        self.pushButtonRemoveProduct.setText(_translate("MainWindow", "Видалити продукт"))
        self.pushButtonRemoveDish.setText(_translate("MainWindow", "Видалити страву"))
        self.labelStatistic.setText(_translate("MainWindow", "TextLabel"))
        self.pushButtonShowStatistics.setText(_translate("MainWindow", "Показати статистику"))

    def add_item(self):
        item_type, ok = QtWidgets.QInputDialog.getItem(
            self.centralwidget, "Add Item", "Select item type:", ("Product", "Dish"), 0, False)
        if ok and item_type:
            if item_type == "Product":
                self.add_product()
            else:
                self.add_dish()
    def add_product(self):
        product_name, ok = QtWidgets.QInputDialog.getText(
            self.centralwidget, "Add Product", "Enter product name:")

        if ok and product_name:
            product_quantity, ok = QtWidgets.QInputDialog.getInt(
                self.centralwidget, "Додати продукт", "Введіть кількість:", 1, 1, 1000, 1)
            if ok:
                product_expiration_date, ok = QtWidgets.QInputDialog.getText(
                    self.centralwidget, "Додати продукт", "Введіть дату закінчення терміну придатності (YYYY-MM-DD):")
                if ok and product_expiration_date:
                    try:
                        expiration_date = datetime.strptime(
                            product_expiration_date, "%Y-%m-%d")
                        new_product = Product(
                            product_name, product_quantity, expiration_date)
                        self.refrigerator.add_food(new_product)
                        self.update_product_list()
                        QtWidgets.QMessageBox.information(
                            self.centralwidget, "Успіх", f"{product_name} додано до холодильника.")
                    except ValueError:
                        QtWidgets.QMessageBox.warning(
                            self.centralwidget, "Помилка", "Невірний формат дати закінчення терміну придатності.")

    def add_dish(self):
        dish_name, ok = QtWidgets.QInputDialog.getText(
            self.centralwidget, "Add Dish", "Enter dish name:")
        if ok and dish_name:
            ingredients = []
            for food in self.refrigerator._foods:
                if isinstance(food, Product):
                    ingredients.append(food)

            ingredient_dialog = QtWidgets.QDialog()
            ingredient_dialog.setWindowTitle("Select Ingredients")
            ingredient_layout = QtWidgets.QVBoxLayout()

            # Create checkboxes for each ingredient
            ingredient_quantity_inputs = {}
            for ingredient in ingredients:
                checkbox = QtWidgets.QCheckBox(ingredient.name)
                ingredient_layout.addWidget(checkbox)

                quantity_label = QtWidgets.QLabel("Quantity:")
                quantity_input = QtWidgets.QSpinBox()
                quantity_input.setMinimum(1)
                quantity_input.setMaximum(1000)
                ingredient_layout.addWidget(quantity_label)
                ingredient_layout.addWidget(quantity_input)

                ingredient_quantity_inputs[ingredient] = quantity_input

            add_button = QtWidgets.QPushButton("Add Dish")
            add_button.clicked.connect(lambda: self.add_selected_dish(dish_name, ingredient_quantity_inputs))
            ingredient_layout.addWidget(add_button)
            ingredient_dialog.setLayout(ingredient_layout)

            ingredient_dialog.exec_()

    def add_selected_dish(self, dish_name, ingredient_quantity_inputs):
        selected_ingredients = []
        for ingredient, quantity_input in ingredient_quantity_inputs.items():
            if quantity_input.value() > 0:
                selected_ingredients.extend([ingredient] * quantity_input.value())

        new_dish = Dish(dish_name, selected_ingredients)
        self.refrigerator.add_food(new_dish)
        self.update_dish_list()

        for ingredient in selected_ingredients:
            ingredient.quantity -= 1
            if ingredient.quantity == 0:
                self.refrigerator.remove_food(ingredient)
        self.update_product_list()

        QtWidgets.QMessageBox.information(
            self.centralwidget, "Success", f"{dish_name} added to the refrigerator.")

    def edit_product_or_dish(self):
        selected_index = self.listViewProducts.currentIndex().row()
        if selected_index >= 0:
            selected_food = self.refrigerator._foods[selected_index]
            if isinstance(selected_food, Product):
                new_name, ok = QtWidgets.QInputDialog.getText(
                    self.centralwidget, "Редагувати продукт", "Введіть нову назву продукту:")
                if ok and new_name:
                    new_quantity, ok = QtWidgets.QInputDialog.getInt(
                        self.centralwidget, "Редагувати продукт", "Введіть нову кількість:", 1, 1, 1000, 1)
                    if ok:
                        new_expiration_date, ok = QtWidgets.QInputDialog.getText(
                            self.centralwidget, "Редагувати продукт",
                            "Введіть нову дату закінчення терміну придатності (YYYY-MM-DD):")
                        if ok and new_expiration_date:
                            try:
                                new_expiration_date = datetime.strptime(
                                    new_expiration_date, "%Y-%m-%d")
                                selected_food._name = new_name
                                selected_food._quantity = new_quantity
                                selected_food._expiration_date = new_expiration_date
                                self.update_product_list()
                                QtWidgets.QMessageBox.information(
                                    self.centralwidget, "Успіх",
                                    f"Продукт '{selected_food.name}' успішно відредаговано.")
                            except ValueError:
                                QtWidgets.QMessageBox.warning(
                                    self.centralwidget, "Помилка",
                                    "Невірний формат дати закінчення терміну придатності.")
        else:
            selected_index = self.listViewDish.currentIndex().row()
            if selected_index >= 0:
                selected_dish = self.refrigerator._foods[selected_index]
                new_name, ok = QtWidgets.QInputDialog.getText(
                    self.centralwidget, "Редагувати страву", "Введіть нову назву страви:")
                if ok and new_name:
                    new_ingredients = []
                    for food in self.refrigerator._foods:
                        if isinstance(food, Product):
                            new_ingredients.append(food)
                    ingredient_dialog = QtWidgets.QDialog()
                    ingredient_dialog.setWindowTitle("Оберіть нові інгредієнти")
                    ingredient_layout = QtWidgets.QVBoxLayout()
                    for ingredient in new_ingredients:
                        checkbox = QtWidgets.QCheckBox(ingredient.name)
                        ingredient_layout.addWidget(checkbox)
                    add_button = QtWidgets.QPushButton("Оновити страву")
                    add_button.clicked.connect(ingredient_dialog.accept)
                    ingredient_layout.addWidget(add_button)
                    ingredient_dialog.setLayout(ingredient_layout)
                    if ingredient_dialog.exec_():
                        selected_ingredients = [new_ingredients[i] for i in range(len(new_ingredients)) if
                                                ingredient_layout.itemAt(i).widget().isChecked()]
                        selected_dish._name = new_name
                        selected_dish._ingredients = selected_ingredients
                        self.update_dish_list()
                        QtWidgets.QMessageBox.information(
                            self.centralwidget, "Успіх", f"Страва '{selected_dish.name}' успішно відредагована.")

    def remove_product(self):
        selected_index = self.listViewProducts.currentIndex().row()
        if selected_index >= 0:
            selected_product = self.refrigerator._foods[selected_index]
            self.refrigerator.remove_food(selected_product)
            self.update_product_list()
            QtWidgets.QMessageBox.information(
                self.centralwidget, "Успіх", f"Продукт '{selected_product.name}' успішно видалено.")

    def remove_dish(self):
        selected_index = self.listViewDish.currentIndex().row()
        if selected_index >= 0:
            selected_dish = self.refrigerator._foods[selected_index]
            self.refrigerator.remove_food(selected_dish)
            self.update_dish_list()
            QtWidgets.QMessageBox.information(
                self.centralwidget, "Успіх", f"Страва '{selected_dish.name}' успішно видалена.")

    def show_statistics(self):
        total_foods, total_dishes, low_stock_products, expired_foods = self.statistics.analyze_foods()
        statistics_text = f"Total Foods: {total_foods}\n"
        statistics_text += f"Total Dishes: {total_dishes}\n\n"

        if low_stock_products:
            statistics_text += "You should buy more of the following products:\n"
            for product_name in low_stock_products:
                statistics_text += f"- {product_name}\n"
            statistics_text += "\n"

        if expired_foods:
            statistics_text += "The following products have expired or are about to expire:\n"
            for product in expired_foods:
                statistics_text += f"- {product.name} (Expiration date: {product.expiration_date.strftime('%Y-%m-%d')})\n"

        self.labelStatistic.setText(statistics_text)

    def update_product_list(self):
        self.products_model.clear()
        for food in self.refrigerator._foods:
            if isinstance(food, Product):
                item = QtGui.QStandardItem(f"{food.name} ({food.quantity})")
                self.products_model.appendRow(item)

    def update_dish_list(self):
        self.dishes_model.clear()
        for food in self.refrigerator._foods:
            if isinstance(food, Dish):
                item = QtGui.QStandardItem(food.name)
                self.dishes_model.appendRow(item)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())