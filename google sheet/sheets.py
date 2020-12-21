import gspread


# Using the service credential which was created in the google
# developer console and downloaded as json file
gc = gspread.service_account(filename='credential.json')

# opening the file using the key instead of filename
sh = gc.open_by_key('1c8GkIHjMkcmapbvEwDkBSQACzChlLROnfPXPlJJ8Txs')

# getting the worksheet 'test'
worksheet = sh.worksheet('test')

# getting all the worksheets in the workbook as a list
list = sh.worksheets()
print(list)

# printing all values of the table
print(worksheet.get_all_values())

# printing first row, index start with 1
print(worksheet.row_values(1))

# printing first column
print(worksheet.col_values(1))

# getting the cell data
print(worksheet.get('A2'))

# getting the range of table as a list
print(worksheet.get('A2:C2'))

# inserting a row with values
RO = ['134568', 'Dakshh Fuel Centre', 'Jeypore']
#worksheet.insert_row(RO, 3)


RO_1 = ['134543', 'Mallik Fuels', 'Sambalpur']
# append to the table
worksheet.append_row(RO_1)

