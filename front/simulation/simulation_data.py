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
    component_names = []

    for cell in self.table_data:

        if cell[0].isdigit():
            self.statusBar().showMessage(
                f'in row {self.table_data.index(cell)+1} name of component cannot be integer!')

        if '' not in cell:

            if all(isinstance(cell[i], str) and cell[i].isdigit() for i in range(1, 8)) and not cell[0].isdigit():
                if cell[0] not in component_names:
                    component_names.append(cell[0])

                table_row_count += 1
                if table_row == table_row_count:
                    save_data(self)

            else:
                self.propertice_next.setStyleSheet(
                    "background-color:rgb(157, 157, 157); color:#FF0000 ;border-radius:6px ;border-style:solid;")
                self.propertice_next.setEnabled(True)

        else:
            self.propertice_next.setStyleSheet(
                "background-color:rgb(157, 157, 157); color:#FF0000 ;border-radius:6px ;border-style:solid;")
            self.propertice_next.setEnabled(True)


def save_data(self):

    self.propertice_next.setStyleSheet(
        "background-color:rgb(157, 157, 157); color:#00FF7F ;border-radius:6px ;border-style:dotted;")
    self.propertice_next.setEnabled(False)

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
        'back/output2.xls', sheet_name='GLS_properties', header=header_names, index=False)
