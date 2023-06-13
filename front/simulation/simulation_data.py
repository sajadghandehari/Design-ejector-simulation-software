from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import pandas as pd

component_names = []


def table_propertise_get_data(self):
    global component_names

    # get the number of rows and columns in the table
    num_rows = self.properties_table.rowCount()
    num_cols = self.properties_table.columnCount()

    # create an empty list to store the table data
    self.table_data = []
    palette = self.statusBar().palette()
    palette.setColor(self.statusBar().foregroundRole(),
                     Qt.red)  # Set the text color to red
    self.statusBar().setPalette(palette)

    # iterate through each cell in the table and append its text to the list
    for row in range(num_rows):
        current_row = []
        for col in range(num_cols):
            item = self.properties_table.item(row, col)
            current_row.append(item.text() if item is not None else "")
        self.table_data.append(current_row)

    self.statusBar().showMessage(f'')

    table_row = len(self.table_data)
    table_row_count = 0

    for cell in self.table_data:

        if cell[0].isdigit():
            self.statusBar().showMessage(
                f'in row {self.table_data.index(cell)+1} name of component cannot be integer!')

        if '' not in cell:

            if all(isinstance(cell[i], str) and cell[i].isdigit() for i in range(1, 8)) and not cell[0].isdigit():
                if cell[0] not in component_names:
                    component_names.append(f'Specific Heat {cell[0]}')

                table_row_count += 1
                if table_row == table_row_count:
                    save_data(self)
                    self.propertice_next.setEnabled(True)
                    print(component_names)

            else:
                self.propertice_next.setStyleSheet(
                    "background-color:rgb(157, 157, 157); color:#FF0000 ;border-radius:6px ;border-style:solid;")
                self.propertice_next.setEnabled(False)
                component_names = []

        else:
            self.propertice_next.setStyleSheet(
                "background-color:rgb(157, 157, 157); color:#FF0000 ;border-radius:6px ;border-style:solid;")
            self.propertice_next.setEnabled(False)
            component_names = []


def save_data(self):

    self.propertice_next.setStyleSheet(
        "background-color:rgb(157, 157, 157); color:#00FF7F ;border-radius:6px ;border-style:dotted;")
    #
    header_names = [
        'n_species',
        'molocular wight of any species',
        'molaur fraction of any species',
        'gas constant for any species per psia-ft.3/(lb-mole)-°R',
        'Formation Enthalpy(ft^2/sec^2)',
        'Vsa (Coefficient of viscosity equation for any species',
        'Vsb (Coefficient of viscosity equation for any species',
        'Vsb (Coefficient of viscosity equation for any species'
    ]

    component_names.insert(0, 'Temperature (R)')
    self.specific_heat_table.setColumnCount(
        len(component_names))  # Set the number of columns
    self.specific_heat_table.setHorizontalHeaderLabels(
        component_names)  # Set the column headers

    row = 0
    for cell in self.table_data:
        if row == 0:
            cell[0] = len(self.table_data)
        else:
            cell[0] = ''

        row += 1

    df = pd.DataFrame(self.table_data)

    # Write the DataFrame to an Excel file
    df.to_excel(
        self.writer, sheet_name='GLS_properties', header=header_names, index=False)
    # self.writer.save()

    # Handel_Buttons(self)


def specific_heat_gas_get_data(self):

    # get the number of rows and columns in the table
    num_rows = self.specific_heat_table.rowCount()
    num_cols = self.specific_heat_table.columnCount()

    # create an empty list to store the table data
    self.table_data = []
    palette = self.statusBar().palette()
    palette.setColor(self.statusBar().foregroundRole(),
                     Qt.red)  # Set the text color to red
    self.statusBar().setPalette(palette)

    # iterate through each cell in the table and append its text to the list
    for row in range(num_rows):
        current_row = []
        for col in range(num_cols):
            item = self.specific_heat_table.item(row, col)
            current_row.append(item.text() if item is not None else "")
        self.table_data.append(current_row)

    self.statusBar().showMessage(f'')

    table_row = len(self.table_data)
    table_row_count = 0

    for cell in self.table_data:

        if '' not in cell:

            if all(isinstance(cell[i], str) and cell[i].isdigit() for i in range(0, num_cols)):

                table_row_count += 1
                if table_row == table_row_count:
                    # save_data(self)
                    print(self.table_data)
                    specific_heat_save_data(self)
                    self.specific_heat_next.setEnabled(True)

            else:
                self.specific_heat_next.setStyleSheet(
                    "background-color:rgb(157, 157, 157); color:#FF0000 ;border-radius:6px ;border-style:solid;")
                self.specific_heat_next.setEnabled(False)

        else:
            self.specific_heat_next.setStyleSheet(
                "background-color:rgb(157, 157, 157); color:#FF0000 ;border-radius:6px ;border-style:solid;")
            self.specific_heat_next.setEnabled(False)


def specific_heat_save_data(self):

    self.specific_heat_next.setStyleSheet(
        "background-color:rgb(157, 157, 157); color:#00FF7F ;border-radius:6px ;border-style:dotted;")

    header_names = ['n_tab']
    for col in range(self.specific_heat_table.columnCount()):
        header_item = self.specific_heat_table.horizontalHeaderItem(col)
        if header_item is not None:
            header_names.append(header_item.text())

    print(component_names)

    count = 0
    for name in component_names:
        if 'Specific Heat' in name:
            new_name = name.replace('Specific Heat', 'Enthalpy')
            component_names[count] = new_name

        count += 1

    self.enthalpy_gas_table.setColumnCount(
        len(component_names))  # Set the number of columns
    self.enthalpy_gas_table.setHorizontalHeaderLabels(
        component_names)  # Set the column headers

    row = 0
    for cell in self.table_data:
        if row == 0:
            cell.insert(0, len(self.table_data))
        else:
            cell.insert(0, '')

        row += 1

    print(self.table_data)

    df = pd.DataFrame(self.table_data)

    # Write the DataFrame to an Excel file
    df.to_excel(
        self.writer, sheet_name='specific heat_gas', header=header_names, index=False)


def enthalpy_gas_get_data(self):

    # get the number of rows and columns in the table
    num_rows = self.enthalpy_gas_table.rowCount()
    num_cols = self.enthalpy_gas_table.columnCount()

    # create an empty list to store the table data
    self.table_data = []
    palette = self.statusBar().palette()
    palette.setColor(self.statusBar().foregroundRole(),
                     Qt.red)  # Set the text color to red
    self.statusBar().setPalette(palette)

    # iterate through each cell in the table and append its text to the list
    for row in range(num_rows):
        current_row = []
        for col in range(num_cols):
            item = self.enthalpy_gas_table.item(row, col)
            current_row.append(item.text() if item is not None else "")
        self.table_data.append(current_row)

    self.statusBar().showMessage(f'')

    table_row = len(self.table_data)
    table_row_count = 0

    for cell in self.table_data:

        if '' not in cell:

            if all(isinstance(cell[i], str) and cell[i].isdigit() for i in range(0, num_cols)):

                table_row_count += 1
                if table_row == table_row_count:
                    # save_data(self)
                    print(self.table_data)
                    enthalpy_gas_save_data(self)
                    self.enthalpy_gas_next.setEnabled(True)
                    print('OOK')

            else:
                self.enthalpy_gas_next.setStyleSheet(
                    "background-color:rgb(157, 157, 157); color:#FF0000 ;border-radius:6px ;border-style:solid;")
                self.enthalpy_gas_next.setEnabled(False)

        else:
            self.enthalpy_gas_next.setStyleSheet(
                "background-color:rgb(157, 157, 157); color:#FF0000 ;border-radius:6px ;border-style:solid;")
            self.enthalpy_gas_next.setEnabled(False)


def enthalpy_gas_save_data(self):

    self.enthalpy_gas_next.setStyleSheet(
        "background-color:rgb(157, 157, 157); color:#00FF7F ;border-radius:6px ;border-style:dotted;")

    header_names = ['n_tab']
    for col in range(self.enthalpy_gas_table.columnCount()):
        header_item = self.enthalpy_gas_table.horizontalHeaderItem(col)
        if header_item is not None:
            header_names.append(header_item.text())

    print(header_names)

    row = 0
    for cell in self.table_data:
        if row == 0:
            cell.insert(0, len(self.table_data))
        else:
            cell.insert(0, '')

        row += 1

    print(self.table_data)

    df = pd.DataFrame(self.table_data)

    # Write the DataFrame to an Excel file
    df.to_excel(
        self.writer, sheet_name='entalpy_gas', header=header_names, index=False)

    self.writer.close()


def gls_properties_get_data(self):
    pass


def bellow_get_data(self):
    pass
