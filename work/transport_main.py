import pandas as pd
from transport_methods import *
import os
from openpyxl import load_workbook
import openpyxl


os.chdir('D:\Personal\Reports')
# print(os.listdir())
df = pd.read_excel('Monthly Calculation - Transport.xlsx', sheet_name='Master')
net_profit = []
own_profit = []
percent_share = []
nl = "\n"
for index, row in df.iterrows():
    # print(f'{index}-->{row["Owners Share"]}-->{row["RTKM"]}-->{row["TT Details"]}-->{row["No of Trip"]}{nl}')
    net_profit.append(revenue_share(row["Owners Share"], row["RTKM"], row["TT Details"], row["No of Trip"])[0])
    own_profit.append(revenue_share(row["Owners Share"], row["RTKM"], row["TT Details"], row["No of Trip"])[1])
    percent_share.append(revenue_share(row["Owners Share"], row["RTKM"], row["TT Details"], row["No of Trip"])[2])
    # print(f'{net_profit}-->{own_profit}-->{percent_share}')

# print(f'net_profit is: {net_profit}{nl}')
# print(f'own_profit is: {own_profit}{nl}')
# print(f'percentage_share is: {percent_share}{nl}')

df['net profit'] = net_profit
df['own profit'] = own_profit
df['percentage share'] = percent_share

print(df.head())
# Function arguments are: owner_share, rtkm, tt_capacity, no_of_trip
# print(revenue_share(0.08, 1100, 14, 8))

with pd.ExcelWriter('Monthly Calculation - Transport.xlsx', engine='openpyxl') as writer:
    writer.book = load_workbook('Monthly Calculation - Transport.xlsx')
    df.to_excel(writer, index=False)