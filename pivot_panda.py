import pandas as pd
from openpyxl import load_workbook


def cell_to_num(char):
    char = char.upper()
    if char.isalpha():
        num = ord(char) - 64
    else:
        num = 0
    return num


print(cell_to_num('a'))

# Get the file from the downloads folder
path = '/mnt/c/Users/panka/Downloads/Nozzle Sale Report.xlsx'
wb = load_workbook(path)
ws = wb.active

# Delete column O:R
# ws.delete_cols(
# Delete column K:M

# Delete column B:F

# Delete column U:V

# Unmerge cell S1:T1
