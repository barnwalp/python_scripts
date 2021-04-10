import pandas as pd
from transport_methods import *
import os
from openpyxl import load_workbook
import openpyxl


os.chdir('D:\Personal\Reports')
# print(os.listdir())
df = pd.read_excel('Transport Calculation.xlsx', sheet_name='Vehicle')


vehicle_dict = df[['Vehicle Number', 'TT Details']].set_index('Vehicle Number').T.to_dict('list')

# we can remove nan key in dictionary by simple list comprehension based on
# on the fact that nan does not equal itself
vehicle_dict = {k: v for k, v in vehicle_dict.items() if k == k}
for key, value in vehicle_dict.items():
    monthly_fixed_cost = fixed_cost(value[0])/12
    vehicle_dict[key].append(monthly_fixed_cost)

# print(vehicle_dict)

trip_dict = df[['Unique Id', 'Vehicle Number', 'RO Name', 'Owners Share', 'RTKM', 'TT Details', 'No of Trip']].set_index('Unique Id').T.to_dict('list')
# print(trip_dict)
rtkm_rate = {14: 2.85, 22: 2.44}

for key, value in trip_dict.items():
    per_trip_expense = per_trip_cost(value[3], value[4], value[5])
    revenue_per_month = value[3] * value[4] * rtkm_rate[value[4]] * value[5]
    trip_dict[key].append((revenue_per_month))
    trip_dict[key].append(per_trip_expense)

print(trip_dict)
"""
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
"""