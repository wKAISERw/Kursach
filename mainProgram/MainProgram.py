# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainProgram.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1332, 726)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listViewProducts = QtWidgets.QListView(self.centralwidget)
        self.listViewProducts.setGeometry(QtCore.QRect(40, 160, 581, 451))
        self.listViewProducts.setObjectName("listViewProducts")
        self.pushButtonAddItem = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonAddItem.setGeometry(QtCore.QRect(550, 20, 131, 41))
        self.pushButtonAddItem.setStyleSheet("font-size: 8pt;\n"
"")
        self.pushButtonAddItem.setObjectName("pushButtonAddItem")
        self.pushButtonSave = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSave.setGeometry(QtCore.QRect(250, 20, 131, 41))
        self.pushButtonSave.setObjectName("pushButtonSave")
        self.pushButtonLoad = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonLoad.setGeometry(QtCore.QRect(400, 20, 131, 41))
        self.pushButtonLoad.setObjectName("pushButtonLoad")
        self.pushButtonRemove = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonRemove.setGeometry(QtCore.QRect(700, 20, 131, 41))
        self.pushButtonRemove.setStyleSheet("font-size: 8pt;\n"
"")
        self.pushButtonRemove.setObjectName("pushButtonRemove")
        self.pushButtonEdit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonEdit.setGeometry(QtCore.QRect(850, 20, 131, 41))
        self.pushButtonEdit.setObjectName("pushButtonEdit")
        self.labelStatisticCountFood = QtWidgets.QLabel(self.centralwidget)
        self.labelStatisticCountFood.setGeometry(QtCore.QRect(60, 630, 171, 61))
        self.labelStatisticCountFood.setStyleSheet("font-size: 12pt;\n"
"")
        self.labelStatisticCountFood.setObjectName("labelStatisticCountFood")
        self.listViewDish = QtWidgets.QListView(self.centralwidget)
        self.listViewDish.setGeometry(QtCore.QRect(660, 210, 621, 461))
        self.listViewDish.setObjectName("listViewDish")
        self.pushButtonShowStatistics = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonShowStatistics.setGeometry(QtCore.QRect(1000, 20, 161, 41))
        self.pushButtonShowStatistics.setObjectName("pushButtonShowStatistics")
        self.labelCheckAmountOfProducts = QtWidgets.QLabel(self.centralwidget)
        self.labelCheckAmountOfProducts.setGeometry(QtCore.QRect(440, 650, 111, 16))
        self.labelCheckAmountOfProducts.setStyleSheet("font-size: 12pt")
        self.labelCheckAmountOfProducts.setObjectName("labelCheckAmountOfProducts")

        self.lineEditSearch = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditSearch.setGeometry(QtCore.QRect(480, 90, 361, 41))
        self.lineEditSearch.setObjectName("lineEditSearch")
        self.lineEditSearch.setPlaceholderText("Введіть пошуковий запит")

        self.comboBoxSelectionForSearch = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxSelectionForSearch.setGeometry(QtCore.QRect(330, 90, 141, 41))
        self.comboBoxSelectionForSearch.setObjectName("comboBoxSelectionForSearch")
        self.comboBoxSelectionForSearch.addItem("Продукти")
        self.comboBoxSelectionForSearch.addItem("Страви")

        self.pushButtonSearch = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSearch.setGeometry(QtCore.QRect(850, 90, 141, 41))
        self.pushButtonSearch.setStyleSheet("font-size: 16pt;")
        self.pushButtonSearch.setObjectName("pushButtonSearch")
        self.pushButtonSearch.setText("Пошук")


        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButtonAddItem.setText(_translate("MainWindow", "Додати"))
        self.pushButtonSave.setText(_translate("MainWindow", "Зберегти"))
        self.pushButtonLoad.setText(_translate("MainWindow", "Завантажити"))
        self.pushButtonRemove.setText(_translate("MainWindow", "Видалити"))
        self.pushButtonEdit.setText(_translate("MainWindow", "Редагувати"))
        self.labelStatisticCountFood.setText(_translate("MainWindow", "TextLabel"))
        self.pushButtonShowStatistics.setText(_translate("MainWindow", "Переглянути статистику"))
        self.labelCheckAmountOfProducts.setText(_translate("MainWindow", "TextLabel"))
        self.pushButtonSearch.setText(_translate("MainWindow", "Пошук"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
