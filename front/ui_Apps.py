# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Sajad\AP_Dr Rafiei\Finall project\Apps.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1304, 745)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.history_tab = QtWidgets.QPushButton(self.centralwidget)
        self.history_tab.setGeometry(QtCore.QRect(50, 70, 70, 70))
        self.history_tab.setStyleSheet("border: none;")
        self.history_tab.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\Sajad\\AP_Dr Rafiei\\Finall project\\icon/history-36.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.history_tab.setIcon(icon)
        self.history_tab.setIconSize(QtCore.QSize(70, 70))
        self.history_tab.setObjectName("history_tab")
        self.simulation_tab = QtWidgets.QPushButton(self.centralwidget)
        self.simulation_tab.setGeometry(QtCore.QRect(50, 190, 70, 70))
        self.simulation_tab.setStyleSheet("border: none;")
        self.simulation_tab.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("c:\\Users\\Sajad\\AP_Dr Rafiei\\Finall project\\icon/5346252.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.simulation_tab.setIcon(icon1)
        self.simulation_tab.setIconSize(QtCore.QSize(70, 70))
        self.simulation_tab.setObjectName("simulation_tab")
        self.setting_tab = QtWidgets.QPushButton(self.centralwidget)
        self.setting_tab.setGeometry(QtCore.QRect(50, 300, 70, 70))
        self.setting_tab.setStyleSheet("border: none;")
        self.setting_tab.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("c:\\Users\\Sajad\\AP_Dr Rafiei\\Finall project\\icon/Settings-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setting_tab.setIcon(icon2)
        self.setting_tab.setIconSize(QtCore.QSize(70, 70))
        self.setting_tab.setObjectName("setting_tab")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(160, 20, 1100, 681))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(100, 190, 900, 371))
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setAutoScrollMargin(16)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.DashLine)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(423)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(100, 130, 271, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 25 12pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.tab, "")
        self.Simulation = QtWidgets.QWidget()
        self.Simulation.setObjectName("Simulation")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.Simulation)
        self.tabWidget_2.setGeometry(QtCore.QRect(20, 20, 1050, 620))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.tabWidget_2.setFont(font)
        self.tabWidget_2.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_2 = QtWidgets.QLabel(self.tab_3)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 281, 30))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit.setGeometry(QtCore.QRect(330, 80, 100, 30))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_5.setGeometry(QtCore.QRect(790, 440, 131, 28))
        self.pushButton_5.setObjectName("pushButton_5")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget_2.setGeometry(QtCore.QRect(20, 160, 901, 271))
        self.tableWidget_2.setRowCount(7)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(7)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, item)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(160)
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.tab_4)
        self.tableWidget_3.setGeometry(QtCore.QRect(120, 150, 800, 350))
        self.tableWidget_3.setRowCount(12)
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        self.tableWidget_3.horizontalHeader().setDefaultSectionSize(374)
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_6.setGeometry(QtCore.QRect(800, 510, 121, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        self.tabWidget_2.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tableWidget_4 = QtWidgets.QTableWidget(self.tab_5)
        self.tableWidget_4.setGeometry(QtCore.QRect(120, 150, 800, 350))
        self.tableWidget_4.setRowCount(12)
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, item)
        self.tableWidget_4.horizontalHeader().setDefaultSectionSize(374)
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_7.setGeometry(QtCore.QRect(800, 510, 121, 31))
        self.pushButton_7.setObjectName("pushButton_7")
        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.label_3 = QtWidgets.QLabel(self.tab_6)
        self.label_3.setGeometry(QtCore.QRect(35, 120, 231, 30))
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_6)
        self.lineEdit_2.setGeometry(QtCore.QRect(385, 120, 113, 28))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_6)
        self.lineEdit_3.setGeometry(QtCore.QRect(385, 180, 113, 28))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(self.tab_6)
        self.label_4.setGeometry(QtCore.QRect(35, 180, 231, 30))
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_6)
        self.lineEdit_4.setGeometry(QtCore.QRect(385, 240, 113, 28))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_5 = QtWidgets.QLabel(self.tab_6)
        self.label_5.setGeometry(QtCore.QRect(35, 240, 321, 30))
        self.label_5.setObjectName("label_5")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_6)
        self.lineEdit_5.setGeometry(QtCore.QRect(385, 300, 113, 28))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_6 = QtWidgets.QLabel(self.tab_6)
        self.label_6.setGeometry(QtCore.QRect(35, 300, 231, 30))
        self.label_6.setObjectName("label_6")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab_6)
        self.lineEdit_6.setGeometry(QtCore.QRect(385, 360, 113, 28))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_7 = QtWidgets.QLabel(self.tab_6)
        self.label_7.setGeometry(QtCore.QRect(35, 360, 231, 30))
        self.label_7.setObjectName("label_7")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.tab_6)
        self.lineEdit_7.setGeometry(QtCore.QRect(390, 420, 113, 28))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_8 = QtWidgets.QLabel(self.tab_6)
        self.label_8.setGeometry(QtCore.QRect(40, 420, 261, 30))
        self.label_8.setObjectName("label_8")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.tab_6)
        self.lineEdit_8.setGeometry(QtCore.QRect(390, 480, 113, 28))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_9 = QtWidgets.QLabel(self.tab_6)
        self.label_9.setGeometry(QtCore.QRect(40, 480, 231, 30))
        self.label_9.setObjectName("label_9")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.tab_6)
        self.lineEdit_18.setGeometry(QtCore.QRect(890, 180, 113, 28))
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.label_19 = QtWidgets.QLabel(self.tab_6)
        self.label_19.setGeometry(QtCore.QRect(580, 180, 231, 30))
        self.label_19.setObjectName("label_19")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.tab_6)
        self.lineEdit_19.setGeometry(QtCore.QRect(890, 240, 113, 28))
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.label_20 = QtWidgets.QLabel(self.tab_6)
        self.label_20.setGeometry(QtCore.QRect(580, 240, 231, 30))
        self.label_20.setObjectName("label_20")
        self.lineEdit_20 = QtWidgets.QLineEdit(self.tab_6)
        self.lineEdit_20.setGeometry(QtCore.QRect(890, 300, 113, 28))
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.label_21 = QtWidgets.QLabel(self.tab_6)
        self.label_21.setGeometry(QtCore.QRect(580, 300, 180, 30))
        self.label_21.setObjectName("label_21")
        self.lineEdit_21 = QtWidgets.QLineEdit(self.tab_6)
        self.lineEdit_21.setGeometry(QtCore.QRect(890, 390, 113, 28))
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.label_22 = QtWidgets.QLabel(self.tab_6)
        self.label_22.setGeometry(QtCore.QRect(580, 360, 281, 81))
        self.label_22.setWordWrap(True)
        self.label_22.setObjectName("label_22")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.tab_6)
        self.lineEdit_17.setGeometry(QtCore.QRect(890, 120, 113, 28))
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.label_18 = QtWidgets.QLabel(self.tab_6)
        self.label_18.setGeometry(QtCore.QRect(580, 120, 231, 30))
        self.label_18.setObjectName("label_18")
        self.tabWidget_2.addTab(self.tab_6, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableWidget_5 = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_5.setGeometry(QtCore.QRect(120, 150, 800, 350))
        self.tableWidget_5.setRowCount(12)
        self.tableWidget_5.setObjectName("tableWidget_5")
        self.tableWidget_5.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(2, item)
        self.tableWidget_5.horizontalHeader().setDefaultSectionSize(249)
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_8.setGeometry(QtCore.QRect(800, 510, 121, 31))
        self.pushButton_8.setObjectName("pushButton_8")
        self.tabWidget_2.addTab(self.tab_2, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.tableWidget_6 = QtWidgets.QTableWidget(self.tab_7)
        self.tableWidget_6.setGeometry(QtCore.QRect(120, 150, 800, 350))
        self.tableWidget_6.setRowCount(12)
        self.tableWidget_6.setObjectName("tableWidget_6")
        self.tableWidget_6.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(1, item)
        self.tableWidget_6.horizontalHeader().setDefaultSectionSize(374)
        self.pushButton_9 = QtWidgets.QPushButton(self.tab_7)
        self.pushButton_9.setGeometry(QtCore.QRect(800, 510, 121, 31))
        self.pushButton_9.setObjectName("pushButton_9")
        self.tabWidget_2.addTab(self.tab_7, "")
        self.tabWidget.addTab(self.Simulation, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.groupBox = QtWidgets.QGroupBox(self.tab_8)
        self.groupBox.setGeometry(QtCore.QRect(30, 70, 500, 550))
        self.groupBox.setWhatsThis("")
        self.groupBox.setStyleSheet("font: 60 10pt \"Roboto Black\";\n"
"")
        self.groupBox.setObjectName("groupBox")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(60, 140, 111, 31))
        self.label_10.setStyleSheet("font: 9pt \"Myanmar Text\";")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(60, 210, 111, 31))
        self.label_11.setStyleSheet("font: 9pt \"Myanmar Text\";")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(60, 280, 111, 31))
        self.label_12.setStyleSheet("font: 9pt \"Myanmar Text\";")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setGeometry(QtCore.QRect(60, 350, 131, 31))
        self.label_13.setStyleSheet("font: 9pt \"Myanmar Text\";")
        self.label_13.setObjectName("label_13")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_9.setGeometry(QtCore.QRect(250, 140, 170, 30))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_10.setGeometry(QtCore.QRect(250, 280, 170, 30))
        self.lineEdit_10.setText("")
        self.lineEdit_10.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_11.setGeometry(QtCore.QRect(250, 210, 170, 30))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_12.setGeometry(QtCore.QRect(250, 350, 170, 30))
        self.lineEdit_12.setText("")
        self.lineEdit_12.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.pushButton_10 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_10.setGeometry(QtCore.QRect(140, 440, 190, 35))
        self.pushButton_10.setStyleSheet("font: 9pt \"MS Shell Dlg 2\";")
        self.pushButton_10.setObjectName("pushButton_10")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_8)
        self.groupBox_2.setGeometry(QtCore.QRect(560, 70, 500, 550))
        self.groupBox_2.setStyleSheet("font: 87 11pt \"Roboto Black\";")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_24 = QtWidgets.QLabel(self.groupBox_2)
        self.label_24.setGeometry(QtCore.QRect(40, 80, 271, 31))
        self.label_24.setObjectName("label_24")
        self.classic = QtWidgets.QPushButton(self.groupBox_2)
        self.classic.setGeometry(QtCore.QRect(40, 140, 31, 31))
        self.classic.setStyleSheet("QPushButton {\n"
"    border-radius: 15px;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #d5d5d5\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"")
        self.classic.setText("")
        self.classic.setObjectName("classic")
        self.dark_blue = QtWidgets.QPushButton(self.groupBox_2)
        self.dark_blue.setGeometry(QtCore.QRect(40, 200, 31, 31))
        self.dark_blue.setStyleSheet("QPushButton {\n"
"    border-radius: 15px;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #162d44\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"")
        self.dark_blue.setText("")
        self.dark_blue.setObjectName("dark_blue")
        self.mnjaromix = QtWidgets.QPushButton(self.groupBox_2)
        self.mnjaromix.setGeometry(QtCore.QRect(40, 260, 31, 31))
        self.mnjaromix.setStyleSheet("QPushButton {\n"
"    border-radius: 15px;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #7bd3a3\n"
"        );\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"")
        self.mnjaromix.setText("")
        self.mnjaromix.setObjectName("mnjaromix")
        self.label_25 = QtWidgets.QLabel(self.groupBox_2)
        self.label_25.setGeometry(QtCore.QRect(90, 140, 71, 31))
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.groupBox_2)
        self.label_26.setGeometry(QtCore.QRect(90, 200, 91, 31))
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.groupBox_2)
        self.label_27.setGeometry(QtCore.QRect(90, 260, 121, 31))
        self.label_27.setStyleSheet("")
        self.label_27.setObjectName("label_27")
        self.tabWidget.addTab(self.tab_8, "")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.tabWidget.addTab(self.tab_9, "")
        self.setting_tab.raise_()
        self.tabWidget.raise_()
        self.history_tab.raise_()
        self.simulation_tab.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1304, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Column"))
        self.label.setText(_translate("MainWindow", "Recent WorkSpace :"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "History"))
        self.label_2.setText(_translate("MainWindow", "The number of types of injected gas :"))
        self.pushButton_5.setText(_translate("MainWindow", "OK"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Molecular Weight"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Mole fraction"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Gas constant"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Enthalpy of formation"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Constant A"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Constant B"))
        item = self.tableWidget_2.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Constant C"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("MainWindow", "Gas Properties"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Specific Heat"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Temperature (R)"))
        self.pushButton_6.setText(_translate("MainWindow", "OK"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "Specific heat-gas"))
        item = self.tableWidget_4.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Specific Enthalpy"))
        item = self.tableWidget_4.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Temperature (R)"))
        self.pushButton_7.setText(_translate("MainWindow", "OK"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), _translate("MainWindow", "Enthalpy-gas"))
        self.label_3.setText(_translate("MainWindow", "Environment Temperature(R) :"))
        self.label_4.setText(_translate("MainWindow", "Environment Pressure(Psig) :"))
        self.label_5.setText(_translate("MainWindow", "Installation height of operating valve(Mft) : "))
        self.label_6.setText(_translate("MainWindow", "Bellows Pressure(Psig) :"))
        self.label_7.setText(_translate("MainWindow", "Fenrit Bellows tension(Psig) :"))
        self.label_8.setText(_translate("MainWindow", "Cross section of Bellows(in^2) :"))
        self.label_9.setText(_translate("MainWindow", "Cross section of Pilot(in^2) :"))
        self.label_19.setText(_translate("MainWindow", "API gravity :"))
        self.label_20.setText(_translate("MainWindow", "Production tube(in) :"))
        self.label_21.setText(_translate("MainWindow", "Orifice diameter(in) :"))
        self.label_22.setText(_translate("MainWindow", "The angle of the axis of the production tube and the analos with the vertical axis :"))
        self.label_18.setText(_translate("MainWindow", "Water cut :"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), _translate("MainWindow", "GLS Properties "))
        item = self.tableWidget_5.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Injection pressure(Psig)"))
        item = self.tableWidget_5.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Well pressure changes(Psig)"))
        item = self.tableWidget_5.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Surface temperature (R)"))
        self.pushButton_8.setText(_translate("MainWindow", "OK"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), _translate("MainWindow", "GLS Properties page 2"))
        item = self.tableWidget_6.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Bellows Phenrite stress changes(Psig)"))
        item = self.tableWidget_6.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Length change(in)"))
        self.pushButton_9.setText(_translate("MainWindow", "OK"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), _translate("MainWindow", "Bellow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Simulation), _translate("MainWindow", "Simulation"))
        self.groupBox.setTitle(_translate("MainWindow", "Add new User"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">User Name</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Email</span></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Password</span></p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Password Again</span></p></body></html>"))
        self.pushButton_10.setText(_translate("MainWindow", "Add User"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Themes"))
        self.label_24.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">You can choose your theme :</span></p></body></html>"))
        self.label_25.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Classic</span></p></body></html>"))
        self.label_26.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Dark</span></p></body></html>"))
        self.label_27.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Manjaro mix</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), _translate("MainWindow", "setting"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), _translate("MainWindow", "Page"))
import icons_rc
