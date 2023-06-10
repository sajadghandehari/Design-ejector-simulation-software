from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

from PyQt5.uic import loadUiType

ui, _ = loadUiType('Apps.ui')
create_user, _ = loadUiType('Createusername.ui')
login, _ = loadUiType('Login.ui')


class Login(QMainWindow, login):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.setWindowTitle("Login page")
        self.setWindowIcon(QIcon('python.png'))

        self.Handel_Buttons()

    def handel_login(self):
        username = self.username.text()
        password = self.password.text()
        print(username, password)

    def Handel_Buttons(self):

        self.LoginButton.clicked.connect(self.login)
        self.CreateButton.clicked.connect(self.create_user)

    def login(self):
        self.window = MainApp()
        self.hide()
        self.window.show()
        app.exec_()

    def create_user(self):
        self.window = CreateUser()
        self.hide()
        self.window.show()
        app.exec_()


class CreateUser(QMainWindow, create_user):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.setWindowTitle("Create User page")
        self.setWindowIcon(QIcon('python.png'))

        self.Handel_Buttons()

    def Handel_Buttons(self):

        self.CreateButton.clicked.connect(self.create_user)

    def create_user(self):
        self.window = MainApp()
        self.hide()
        self.window.show()
        app.exec_()


class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_UI_Changes()
        self.Handel_Buttons()
        self.setWindowTitle("Ejector Simulation App")
        self.setWindowIcon(QIcon('python.png'))

    def Handel_UI_Changes(self):
        self.tabWidget.tabBar().setVisible(False)

    def Handel_Buttons(self):

        self.history_tab.clicked.connect(self.History_Tab)
        self.simulation_tab.clicked.connect(self.Simulation_Tab)
        self.setting_tab.clicked.connect(self.setting_Tab)
        self.classic.clicked.connect(self.calasic_theme)
        self.dark_blue.clicked.connect(self.dark_blue_theme)
        self.mnjaromix.clicked.connect(self.mnjaromix_theme)
        self.gas_propertice_input.returnPressed.connect(
            self.table_propertise_get_data_set_row)
        self.properties_table.cellChanged.connect(
            self.table_propertise_get_data)

        # self.pushButton5.clicked.connect(0,self.tab)
        # for i in range(5):
        #     self.tabWidget_2.setTabEnabled(i+1, False)

    def table_propertise_get_data(self):

        # get the number of rows and columns in the table
        num_rows = self.properties_table.rowCount()
        num_cols = self.properties_table.columnCount()

        # create an empty list to store the table data
        table_data = []

        # iterate through each cell in the table and append its text to the list
        for row in range(num_rows):
            current_row = []
            for col in range(num_cols):
                item = self.properties_table.item(row, col)
                current_row.append(item.text() if item is not None else "")
            table_data.append(current_row)

        for cell in table_data:

            if '' not in cell:
                print(table_data)
                self.propertice_next.setStyleSheet(
                    "background-color:#778899; color:#00FF7F ;border-radius:6px ;border-style:solid;")
            else:
                self.propertice_next.setStyleSheet(
                    "background-color:#778899; color:#FF0000 ;border-radius:6px ;border-style:solid;")

    def History_Tab(self):
        self.tabWidget.setCurrentIndex(0)

    def Simulation_Tab(self):
        self.tabWidget.setCurrentIndex(1)
        text = self.gas_propertice_input.text()
        print(text)

    def table_propertise_get_data_set_row(self):
        print('OK')
        row_count = self.gas_propertice_input.text()

        self.properties_table.setRowCount(int(row_count))
        # self.properties_table.insertRow(2)

    def setting_Tab(self):
        self.tabWidget.setCurrentIndex(2)

    def calasic_theme(self):
        style = open('themes/classic.css', 'r')
        styles = style.read()
        self.setStyleSheet(styles)

    def mnjaromix_theme(self):
        style = open('themes/ManjaroMix.css', 'r')
        styles = style.read()
        self.setStyleSheet(styles)

    def dark_blue_theme(self):
        style = open('themes/dark_blue.css', 'r')
        styles = style.read()
        self.setStyleSheet(styles)

    def tab(self):
        self.tabWidget.setTabEnabled(1, False)
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec_()

"C:/Users/Sajad/Desktop/pic.avif"
