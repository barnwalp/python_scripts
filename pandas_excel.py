import pandas as pd
from openpyxl import load_workbook


# Get the data from the csv file
# for tab separated file, second argument to be passed as
# delimiter='\t'
df = pd.read_csv('pokemon_data.csv')
# Print the loaded data
# print(df)

# printing top 3 and bottom 3 rows of the loaded data
# print(df.head(3))
# print(df.tail(3))

wb = load_workbook('empty_book.xlsx')

# loading excel file
df_xlsx = pd.read_excel('empty_book.xlsx', sheet_name='Data')
# print(df_xlsx)
