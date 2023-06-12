def setting_page_theme(self, color_A, color_B, color_C, color_D):

    # setting page

    self.setStyleSheet(f"background-color:{color_A};")

    self.tabWidget.setStyleSheet(f"background-color:{color_B};")
    self.groupBox_2.setStyleSheet(f"background-color:{color_B};")
    self.groupBox.setStyleSheet(
        f"background-color:{color_B};font: 87 9pt 'Roboto Black';")

    self.create_username.setStyleSheet(
        f"background-color:{color_C};color: rgb(34, 40, 49);border-radius:5px;font: 75 8pt 'Calibri (Body)';")
    self.create_gmail.setStyleSheet(
        f"background-color:{color_C};color: rgb(34, 40, 49);border-radius:5px;font: 75 8pt 'Calibri (Body)';")
    self.create_password.setStyleSheet(
        f"background-color:{color_C};color: rgb(34, 40, 49);border-radius:5px;font: 75 8pt 'Calibri (Body)';")

    self.label_10.setStyleSheet(
        f"color:{color_D};font: 87 11pt 'Roboto Black';")
    self.label_11.setStyleSheet(f"color:{color_D};")
    self.label_12.setStyleSheet(f"color:{color_D};")
    self.label_13.setStyleSheet(f"color:{color_D};")
    self.label_24.setStyleSheet(f"color:{color_D};")
    self.label_25.setStyleSheet(f"color:{color_D};")
    self.label_26.setStyleSheet(f"color:{color_D};")
    self.label_27.setStyleSheet(f"color:{color_D};")
    self.label_14.setStyleSheet(f"color:{color_D};")


def Simulation_page_theme(self, color_A, color_B, color_C, color_D):

    # simulation page
    self.tabWidget_2.setStyleSheet(f"background-color:{color_B};")
    self.tabWidget_2.tabBar().setStyleSheet(f"background-color: {color_C};")

    # alternate-background-color: {color_D};
    self.properties_table.setStyleSheet(f"""
        QTableWidget {{
            background-color: {color_D};
            border-color: {color_C};
            alternate-background-color: {color_C};
        }}
        QTableWidget::item:selected {{
            background-color: {color_D};
        }}
        QHeaderView::section {{
            background-color: {color_C};
        }}
    """)

    table_widgets = [self.tableWidget_3, self.tableWidget_4,
                     self.tableWidget_5, self.tableWidget_6]

    for table_widget in table_widgets:
        table_widget.setStyleSheet(f"""
            QTableWidget {{
                background-color: {color_D};
                border-color: {color_C};
                alternate-background-color: {color_C};
            }}
            QTableWidget::item:selected {{
                background-color: {color_D};
            }}
            QHeaderView::section {{
                background-color: {color_C};
            }}
        """)

    self.gas_propertice_input.setStyleSheet(
        f"background-color:{color_C};color: rgb(34, 40, 49);border-radius:5px;font: 75 8pt 'Calibri (Body)';")
    if color_D == 'rgb(248, 240, 223)':
        color_D = 'rgb(34, 40, 49)'

    label_ranges = [(2, 10), (18, 23)]
    for start, end in label_ranges:
        for i in range(start, end):
            label = getattr(self, f"label_{i}")
            label.setStyleSheet(
                f"color:{color_D};font: 87 9pt 'Roboto Black';")

    line_edit_ranges = [(2, 9), (17, 22)]
    for start, end in line_edit_ranges:
        for i in range(start, end):
            line_edit = getattr(self, f"lineEdit_{i}")
            line_edit.setStyleSheet(
                f"background-color:{color_C};color: rgb(34, 40, 49);border-radius:5px;font: 75 8pt 'Calibri (Body)';"
            )


def History_page_theme(self, color_A, color_B, color_C, color_D):

    self.tableWidget.setStyleSheet(f"""
        QTableWidget {{
            background-color: {color_D};
            border-color: {color_C};
            alternate-background-color: {color_C};
        }}
        QTableWidget::item:selected {{
            background-color: {color_D};
        }}
        QHeaderView::section {{
            background-color: {color_C};
        }}
    """)

    if color_D == 'rgb(248, 240, 223)':
        color_D = 'rgb(34, 40, 49)'

    self.label.setStyleSheet(f"color:{color_D};")
