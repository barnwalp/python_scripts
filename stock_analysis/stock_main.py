from working_with_api import *


# Type of fundamental reports (3rd argument of the function):
# 1. balance-sheet/restated
# 2. income-statement/restated
# 3. cashflow-statement/restated
# 4. statistics

# Type of endpoints (2nd argument of the function)
# 1. fundamentals/yearly
# 2. keyratio
get_stock_data('IOC', 'fundamentals/yearly', 'balance-sheet/restated')
