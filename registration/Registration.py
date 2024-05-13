from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
from Login import Ui_Dialog
# Existing code...

class Ui_RegistrationDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(524, 526)
        Dialog.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(170, 85, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.labelRegistration = QtWidgets.QLabel(Dialog)
        self.labelRegistration.setGeometry(QtCore.QRect(90, 80, 341, 61))
        self.labelRegistration.setStyleSheet("font-size:28pt;\n"
"background-color:none;")
        self.labelRegistration.setObjectName("labelRegistration")
        self.RegistrationLabelEmail = QtWidgets.QLabel(Dialog)
        self.RegistrationLabelEmail.setGeometry(QtCore.QRect(50, 230, 71, 31))
        self.RegistrationLabelEmail.setStyleSheet("font-size:15pt;\n"
"background: none;\n"
"")
        self.RegistrationLabelEmail.setObjectName("RegistrationLabelEmail")
        self.RegistrationLabelPassword = QtWidgets.QLabel(Dialog)
        self.RegistrationLabelPassword.setGeometry(QtCore.QRect(50, 299, 111, 31))
        self.RegistrationLabelPassword.setStyleSheet("font-size:15pt;\n"
"background: none;")
        self.RegistrationLabelPassword.setObjectName("RegistrationLabelPassword")
        self.RegistrationLineEditEmail = QtWidgets.QLineEdit(Dialog)
        self.RegistrationLineEditEmail.setGeometry(QtCore.QRect(250, 231, 221, 31))
        self.RegistrationLineEditEmail.setStyleSheet("font-size:15pt\n"
"")
        self.RegistrationLineEditEmail.setObjectName("RegistrationLineEditEmail")
        self.RegistrationLineEditPassword = QtWidgets.QLineEdit(Dialog)
        self.RegistrationLineEditPassword.setGeometry(QtCore.QRect(250, 300, 221, 31))
        self.RegistrationLineEditPassword.setStyleSheet("font-size:15pt")
        self.RegistrationLineEditPassword.setObjectName("RegistrationLineEditPassword")
        self.pushButtonRegistration = QtWidgets.QPushButton(Dialog)
        self.pushButtonRegistration.setGeometry(QtCore.QRect(180, 410, 161, 41))
        self.pushButtonRegistration.setStyleSheet("font-size:16pt;")
        self.pushButtonRegistration.setObjectName("pushButtonRegistration")
        self.pushButtonBack = QtWidgets.QPushButton(Dialog)
        self.pushButtonBack.setGeometry(QtCore.QRect(50, 410, 121, 41))
        self.pushButtonBack.setStyleSheet("font-size:16pt;")
        self.pushButtonBack.setObjectName("pushButtonBack")
        self.pushButtonBack.setText("Back")
        self.pushButtonBack.clicked.connect(lambda: self.go_back(Dialog))
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButtonRegistration.clicked.connect(self.register)

        self.db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="admin",
            database="AuthorizationDB"
        )
        self.cursor = self.db_connection.cursor()

    def register(self):
        email = self.RegistrationLineEditEmail.text()
        password = self.RegistrationLineEditPassword.text()

        # Check if the email already exists
        self.cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        existing_user = self.cursor.fetchone()
        if existing_user:
            QtWidgets.QMessageBox.warning(None, "Error", "Email already exists.")
            return

        # Insert the new user into the database
        self.cursor.execute("INSERT INTO users (email, password) VALUES (%s, %s)", (email, password))
        self.db_connection.commit()
        QtWidgets.QMessageBox.information(None, "Success", "Registration successful!")

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.labelRegistration.setText(_translate("Dialog", "Create account"))
        self.RegistrationLabelEmail.setText(_translate("Dialog", "Email"))
        self.RegistrationLabelPassword.setText(_translate("Dialog", "Password"))
        self.pushButtonRegistration.setText(_translate("Dialog", "Створити"))
        self.pushButtonBack.setText(_translate("Dialog", "Back"))

    def go_back(self, Dialog):
        self.login_dialog = QtWidgets.QDialog()
        self.ui_login = Ui_Dialog()
        self.ui_login.setupUi(self.login_dialog)
        Dialog.close()
        self.login_dialog.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_RegistrationDialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
