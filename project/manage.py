from back.main import *
from back.main import Run
from simulation.simulation_data import *
from themes.Theme import *
from gmail_service.gmail import send_email
from PyQt5.uic import loadUiType
import pandas
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import random
import sys
import os
import shutil
import datetime


ui, _ = loadUiType('project/Apps.ui')
create_user, _ = loadUiType('project/Createusername.ui')
login, _ = loadUiType('project/Login.ui')
recovery_pass, _ = loadUiType('project/recovery_password.ui')


class Login(QMainWindow, login):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.setWindowTitle("Login page")
        self.setWindowIcon(QIcon('project/python.png'))

        self.Handel_Buttons()

    def handel_login(self):

        username = self.username.text()
        password = self.password.text()

        Users = pandas.read_excel(
            'project/back/User_Information.xlsx', header=None).values

        for user in Users[1:]:
            Username = user[0]
            Password = user[1]
            if Username == username and str(Password) == password:
                print('OK')
                self.login(username)
            else:
                self.meesage_error(
                    (183, 4, 4), "Your Username or Password is not correct !")

    def Handel_Buttons(self):

        self.LoginButton.clicked.connect(self.handel_login)
        self.CreateButton.clicked.connect(self.create_user)
        self.forgot_password.clicked.connect(self.recovery_password)

    def login(self, username):
        self.window = MainApp(username)
        self.hide()
        self.window.show()
        app.exec_()

    def recovery_password(self):
        self.window = RecoveryPassword()
        self.hide()
        self.window.show()
        app.exec_()

    def create_user(self):
        self.window = CreateUser()
        self.hide()
        self.window.show()
        app.exec_()

    def meesage_error(self, color, message):

        palette = self.statusBar().palette()
        palette.setColor(self.statusBar().foregroundRole(),
                         QColor(*color))
        self.statusBar().setPalette(palette)
        self.statusBar().showMessage(message)


class CreateUser(QMainWindow, create_user):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.setWindowTitle("Create User page")
        self.setWindowIcon(QIcon('project/python.png'))

        self.Handel_Buttons()

    def Handel_Buttons(self):

        self.CreateButton.clicked.connect(self.confing_info)
        self.LoginpageButton.clicked.connect(self.login_page)

    def confing_info(self):

        username = self.create_username.text()
        password = self.create_password.text()
        confirm_password = self.confir_password.text()
        gmail = self.create_gmail.text()
        user_from_db = []

        Users = pandas.read_excel(
            'project/back/User_Information.xlsx', header=None).values

        for user in Users[1:]:
            user_from_db.append(user[0])

        if username in user_from_db:
            self.meesage_error(
                (183, 4, 4), 'This username has already been used!')
        elif len(password) < 8:
            self.meesage_error(
                (183, 4, 4), 'Your password must be more than 8 character!')
        elif password != confirm_password:
            self.meesage_error(
                (183, 4, 4), 'Your password and confirm Password must be equal!')
        elif '@gmail.com' not in gmail:
            self.meesage_error(
                (183, 4, 4), 'You must enter valid email address!')
        else:

            df = pandas.read_excel(
                'project/back/User_Information.xlsx', header=None)

            data = [
                [username, password, gmail]
            ]
            new_df = df.append(pandas.DataFrame(data), ignore_index=True)
            # Save the updated DataFrame to the Excel file
            new_df.to_excel('project/back/User_Information.xlsx',
                            header=None, index=False)

            self.create_user(username)

    def create_user(self, username):
        self.window = MainApp(username)
        self.hide()
        self.window.show()
        app.exec_()

    def login_page(self):
        self.window = Login()
        self.window.setFixedSize(600, 300)
        self.hide()
        self.window.show()
        app.exec_()

    def meesage_error(self, color, message):

        palette = self.statusBar().palette()
        palette.setColor(self.statusBar().foregroundRole(),
                         QColor(*color))
        self.statusBar().setPalette(palette)
        self.statusBar().showMessage(message)


class RecoveryPassword(QMainWindow, recovery_pass):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.setWindowTitle("Recovery password")
        self.setWindowIcon(QIcon('project/python.png'))

        self.Handel_Buttons()

    def Handel_Buttons(self):

        self.RecoveryButton.clicked.connect(self.recovery_pass)
        self.LoginpageButton.clicked.connect(self.login_page)

    def recovery_pass(self):

        username = self.username.text()

        Users = pandas.read_excel(
            'project/back/User_Information.xlsx', header=None).values
        df = pd.read_excel('project/back/User_Information.xlsx')

        if username not in Users[1:]:
            self.meesage_error((183, 4, 4), "Your Username not found !")

        for user in Users[1:]:
            if user[0] == username:
                print(user[2])
                random_number = random.randint(10000000, 99999999)
                subject = f"Hi {username}"
                body = f"""We generate and set new password for you, Please do not share with others.
your new password : {random_number}"""
                recipients = user[2]
                sender_email = "ejectorsimulation@gmail.com"
                password = "ljnbjfmpithsywvg"

                send_email(subject, body, sender_email,
                           recipients, password)

                # Save the modified DataFrame back to the Excel file
                df['password'] = df['password'].replace(user[1], random_number)
                df.to_excel('project/back/User_Information.xlsx', index=False)

    def login_page(self):
        self.window = Login()
        self.window.setFixedSize(600, 300)
        self.hide()
        self.window.show()
        app.exec_()

    def meesage_error(self, color, message):

        palette = self.statusBar().palette()
        palette.setColor(self.statusBar().foregroundRole(),
                         QColor(*color))
        self.statusBar().setPalette(palette)
        self.statusBar().showMessage(message)


class MainApp(QMainWindow, ui):
    def __init__(self, username):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_UI_Changes()
        self.Handel_Buttons(username)
        self.setWindowTitle("Ejector Simulation App")
        self.setWindowIcon(QIcon('project/python.png'))
        self.calasic_theme()
        self.update_combobox(username)

        print(self.username)

        # for simulation_number in range(10):
        #     self.file_path = f"project/back/Save_simulation/{username}_simulation_{simulation_number}.xls"
        #     if os.path.exists(self.file_path):
        #         print("File exists", username)
        #     else:
        #         print(f"create {self.file_path}")
        #         self.writer = pd.ExcelWriter(self.file_path)
        #         break
        # self.gls_properties = {}

    def Handel_UI_Changes(self):
        self.tabWidget.tabBar().setVisible(False)

    def Handel_Buttons(self, username):
        self.username = username

        self.history_tab.clicked.connect(self.History_Tab)
        self.simulation_tab.clicked.connect(self.Simulation_Tab)
        self.simulation_tab.setEnabled(False)
        self.setting_tab.clicked.connect(self.setting_Tab)
        self.classic.clicked.connect(self.calasic_theme)
        self.dark_blue.clicked.connect(self.dark_blue_theme)
        self.mnjaromix.clicked.connect(self.mnjaromix_theme)
        self.Earth.clicked.connect(self.Earth_theme)
        self.open_simulation.clicked.connect(self.open_simulations)
        self.insert_file.clicked.connect(self.open_file_dialog)
        self.propertice_next.clicked.connect(self.specific_heat_gas_Tab)
        self.propertice_next.setEnabled(False)
        self.open_new_simulation.clicked.connect(self.Simulation_Tab)

        self.specific_heat_next.clicked.connect(
            lambda: self.tabWidget_2.setCurrentIndex(2))
        self.specific_heat_next.setEnabled(False)
        self.enthalpy_gas_next.clicked.connect(
            lambda: self.tabWidget_2.setCurrentIndex(3))
        self.enthalpy_gas_next.setEnabled(False)
        self.gls_properties_next.clicked.connect(
            lambda: self.tabWidget_2.setCurrentIndex(4))
        self.gls_properties_next.setEnabled(False)
        self.gls_properties2_next.clicked.connect(
            lambda: self.tabWidget_2.setCurrentIndex(5))
        self.gls_properties2_next.setEnabled(False)
        self.calculate_Button.clicked.connect(
            lambda: self.simulation())
        self.calculate_Button.setEnabled(True)

        self.gas_propertice_input.returnPressed.connect(
            lambda: self.set_row('A'))
        self.specific_heat_input.returnPressed.connect(
            lambda: self.set_row('B'))
        self.enthalpy_gas_input.returnPressed.connect(
            lambda: self.set_row('C'))
        self.gls_properties_input.returnPressed.connect(
            lambda: self.set_row('D'))
        self.bellow_input.returnPressed.connect(
            lambda: self.set_row('E'))

        self.lineEdit_2.returnPressed.connect(lambda: self.get_gls_properties(
            'Environment Temperature(R)', self.lineEdit_2))
        self.lineEdit_3.returnPressed.connect(lambda: self.get_gls_properties(
            'Environment Pressure(Psig)', self.lineEdit_3))
        self.lineEdit_4.returnPressed.connect(lambda: self.get_gls_properties(
            'Installation height of operating valve(Mft)', self.lineEdit_4))
        self.lineEdit_5.returnPressed.connect(lambda: self.get_gls_properties(
            'Bellows Pressure(Psig)', self.lineEdit_5))
        self.lineEdit_6.returnPressed.connect(lambda: self.get_gls_properties(
            'Fenrit Bellows tension(Psig)', self.lineEdit_6))
        self.lineEdit_7.returnPressed.connect(lambda: self.get_gls_properties(
            'Cross section of Bellows(in^2)', self.lineEdit_7))
        self.lineEdit_8.returnPressed.connect(lambda: self.get_gls_properties(
            'Cross section of Pilot(in^2)', self.lineEdit_8))
        self.lineEdit_17.returnPressed.connect(lambda: self.get_gls_properties(
            'Water cut', self.lineEdit_17))
        self.lineEdit_18.returnPressed.connect(lambda: self.get_gls_properties(
            'API gravity', self.lineEdit_18))
        self.lineEdit_19.returnPressed.connect(lambda: self.get_gls_properties(
            'Production tube(in)', self.lineEdit_19))
        self.lineEdit_20.returnPressed.connect(lambda: self.get_gls_properties(
            'Orifice diameter(in)', self.lineEdit_20))
        self.lineEdit_21.returnPressed.connect(lambda: self.get_gls_properties(
            'The angle of the axis of the production tube and the analos with the vertical axis', self.lineEdit_21))
        self.lineEdit_22.returnPressed.connect(lambda: self.get_gls_properties(
            'cassing Dia(in)', self.lineEdit_22))

        self.properties_table.cellChanged.connect(
            lambda: table_propertise_get_data(self))

        self.specific_heat_table.cellChanged.connect(
            lambda: specific_heat_gas_get_data(self))

        self.enthalpy_gas_table.cellChanged.connect(
            lambda: enthalpy_gas_get_data(self))

        self.gls_properties_table.cellChanged.connect(
            lambda: gls_properties_get_data(self))

        self.bellow_table.cellChanged.connect(
            lambda: bellow_get_data(self))

    def update_combobox(self, username):

        # self.comboBox.setCurrentIndex(0)

        # Example usage
        directory = "project/back/Save_simulation"
        filename = username

        file_path = self.find_file(directory, filename)

    def find_file(self, directory, filename):
        self.comboBox.clear()
        for root, dirs, files in os.walk(directory):
            count = 0
            for file in files:
                if filename in file:
                    file_path = os.path.join(root, file)
                    self.comboBox.addItem(file)
                    creation_date = self.get_creation_date(file_path)
                    file_item = QTableWidgetItem(file)
                    file_item.setTextAlignment(Qt.AlignCenter)
                    creation_date_item = QTableWidgetItem(creation_date)
                    creation_date_item.setTextAlignment(Qt.AlignCenter)

                    self.tableWidget.setItem(count, 0, file_item)
                    self.tableWidget.setItem(count, 1, creation_date_item)
                    self.tableWidget.setEditTriggers(
                        QAbstractItemView.NoEditTriggers)

                    count += 1

    def open_simulations(self):

        file_path = self.comboBox.currentText()
        run = Run()
        run.run(f"project/back/Save_simulation/{file_path}")

    def get_creation_date(self, file_path):
        if os.path.exists(file_path):
            stat_info = os.stat(file_path)
            creation_timestamp = stat_info.st_ctime
            creation_date = datetime.datetime.fromtimestamp(creation_timestamp)
            formatted_date = creation_date.strftime("%Y-%m-%d %H:%M:%S")
            return formatted_date
        else:
            return None

    def specific_heat_gas_Tab(self):

        self.tabWidget_2.setCurrentIndex(1)

    def History_Tab(self):
        self.tabWidget.setCurrentIndex(0)

    def Simulation_Tab(self):
        self.simulation_tab.setEnabled(True)
        self.tabWidget.setCurrentIndex(1)
        text = self.gas_propertice_input.text()

    def set_row(self, table):

        if table == 'A':
            row_count = self.gas_propertice_input.text()
            self.properties_table.setRowCount(int(row_count))
        if table == 'B':
            row_count = self.specific_heat_input.text()
            self.specific_heat_table.setRowCount(int(row_count))
        if table == 'C':
            row_count = self.enthalpy_gas_input.text()
            self.enthalpy_gas_table.setRowCount(int(row_count))
        if table == 'D':
            row_count = self.gls_properties_input.text()
            self.gls_properties_table.setRowCount(int(row_count))
        if table == 'E':
            row_count = self.bellow_input.text()
            self.bellow_table.setRowCount(int(row_count))

    def setting_Tab(self):
        self.tabWidget.setCurrentIndex(2)

    def get_gls_properties(self, name, value):
        palette = self.statusBar().palette()
        palette.setColor(self.statusBar().foregroundRole(),
                         Qt.red)  # Set the text color to red
        self.statusBar().setPalette(palette)

        if not value.text().isdigit():
            self.meesage_error((183, 4, 4), f'{name} must be integer!')
            value.setText('')
            if name in self.gls_properties:
                self.gls_properties.pop(name)

        else:
            self.meesage_error((183, 4, 4), f'save {name} successfuly')
            if len(self.gls_properties) == 13:
                self.gls_properties_next.setEnabled(True)
                self.gls_properties_next.setStyleSheet(
                    "background-color:rgb(157, 157, 157); color:#00FF7F ;border-radius:6px ;border-style:dotted;")
            else:
                self.gls_properties_next.setEnabled(False)
                self.gls_properties_next.setStyleSheet(
                    "background-color:rgb(157, 157, 157); color:#FF0000 ;border-radius:6px ;border-style:solid;")

    def calasic_theme(self):

        color_A = 'rgb(254, 251, 243)'
        color_B = 'rgb(248, 240, 223)'
        color_C = 'rgb(121, 180, 183)'
        color_D = 'rgb(34, 40, 49)'

        setting_page_theme(self, color_A, color_B, color_C, color_D)
        Simulation_page_theme(self, color_A, color_B, color_C, color_B)
        History_page_theme(self, color_A, color_B, color_C, color_B)

    def Earth_theme(self):

        # earth
        color_A = 'rgb(64, 81, 59)'
        color_B = 'rgb(157, 192, 139)'
        color_C = 'rgb(96, 153, 102)'
        color_D = 'rgb(237, 241, 214)'

        setting_page_theme(self, color_A, color_B, color_C, color_D)
        Simulation_page_theme(self, color_A, color_B, color_C, color_D)
        History_page_theme(self, color_A, color_B, color_C, color_D)

    def mnjaromix_theme(self):

        color_A = 'rgb(6, 41, 37)'
        color_B = 'rgb(4, 74, 66)'
        color_C = 'rgb(58, 145, 136)'
        color_D = 'rgb(184, 225, 221)'

        setting_page_theme(self, color_A, color_B, color_C, color_D)
        Simulation_page_theme(self, color_A, color_B, color_C, color_D)
        History_page_theme(self, color_A, color_B, color_C, color_D)

    def dark_blue_theme(self):

        color_A = 'rgb(35, 41, 49)'
        color_B = 'rgb(57, 62, 70)'
        color_C = 'rgb(78, 204, 163)'
        color_D = 'rgb(238, 238, 238)'

        setting_page_theme(self, color_A, color_B, color_C, color_D)
        Simulation_page_theme(self, color_A, color_B, color_C, color_D)
        History_page_theme(self, color_A, color_B, color_C, color_D)

    def tab(self):
        self.tabWidget.setTabEnabled(1, False)
        pass

    def simulation(self):

        try:

            run = Run()
            # Call the run() method and provide the required arguments
            run.run(self.file_path)
        except:
            try:
                os.remove(self.file_path)
                print(f"The file '{self.file_path}' has been deleted.")
            except FileNotFoundError:
                print(f"The file '{self.file_path}' does not exist.")
            except PermissionError:
                print(
                    f"You do not have permission to delete the file '{self.file_path}'.")
            except Exception as e:
                print(
                    f"An error occurred while deleting the file '{self.file_path}': {e}")

    def open_file_dialog(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Open File")

        if '.xls' in file_path:

            self.file_path = file_path
            source_path = file_path
            destination_folder = "project/back/Save_simulation"

            for simulation_number in range(10):
                path = f"project/back/Save_simulation/{self.username}_simulation_{simulation_number}.xls"
                new_file_name = f"{self.username}_simulation_{simulation_number}.xls"
                if os.path.exists(path):
                    print("File exists", self.username)
                else:
                    self.copy_and_rename_file(
                        source_path, destination_folder, new_file_name)
                    self.update_combobox(self.username)
                    print("Selected file:", file_path)
                    break
        else:
            self.meesage_error((183, 4, 4), 'you must insert an exel file !')

    def copy_and_rename_file(self, source_path, destination_folder, new_file_name):
        # Extract the filename from the source path
        print('OK')
        source_folder, source_filename = os.path.split(source_path)

        # Construct the destination path with the new filename
        destination_path = os.path.join(destination_folder, new_file_name)

        # Copy the file to the destination folder with the new filename
        shutil.copy2(source_path, destination_path)

        # Rename the copied file to the new filename
        renamed_destination_path = os.path.join(
            destination_folder, new_file_name)
        os.rename(destination_path, renamed_destination_path)

        print("File copied and renamed successfully!")

    def meesage_error(self, color, message):
        palette = self.statusBar().palette()
        palette.setColor(self.statusBar().foregroundRole(),
                         QColor(*color))
        self.statusBar().setPalette(palette)
        self.statusBar().showMessage(message)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainApp('Sajad')
    # window = Login()
    window.setFixedSize(1268, 642)
    window.show()
    app.exec_()
