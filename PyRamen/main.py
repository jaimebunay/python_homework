# Lets import the libraries we will use

from pathlib import Path
import csv
# Set file path to read menu and sales data from .csv files
sale_data_path = Path("Resources/sales_data.csv")
menu_data_path = Path("Resources/menu_data.csv")
# Initialize and empty menu list
menu = []

# Use with statement to open the file menu_date.csv in read mode
with open(menu_data_path, 'r') as menu_data: 
    # Use the reader function from csv library 
    # And begin reading menu_data.csv
    menu_reader = csv.reader(menu_data, delimiter = ',')
    # Use next function to skip the header(first row of CSV file)
    next(menu_reader)
    # Loop over the rest of rows and append every row to the menu list object 
    # Outcome should be a list of list of lists
    for row in menu_reader: 
        menu.append(row[:])
#print(menu[:3])

# Initialize another empty list to hold sales data 
sales = []

# Repeat process from above 

with open(sale_data_path, 'r') as sales_data: 
    sales_reader = csv.reader(sales_data, delimiter = ',')
    next(sales_reader)

    for row in sales_reader: 
        sales.append(row[:])

#print(sales[:3])

# Initialize an empty report dictionary to hold the future aggragated per_product result
report = {
    
}

for sales_row in sales: 
    quantity = int(sales_row[3])
    sales_item = sales_row[4]

    if sales_row[4] in report: 
        pass
    else: 
        report[sales_row[4]] = {
        "01-count": 0.0,
        "02-revenue": 0.0,
        "03-cogs": 0.0,
        "04-profit": 0.0,
         }
    for menu_row in menu:
        menu_item = menu_row[0]
        price = float(menu_row[3])
        cost = int(menu_row[4]) 
        profit = price - cost
        if sales_item == menu_item: 
        

            report[sales_item]['01-count'] += quantity
            report[sales_item]['02-revenue'] += price * quantity
            report[sales_item]['03-cogs'] += cost * quantity
            report[sales_item]['04-profit'] += profit * quantity
    
       # else: 
            #print(f"Row: {sales_row}:  {sales_item} is not equals to {menu_item}")



print(report)
#for key in report.keys():
    #print(key)

output = Path("PyRamen_output.txt")

with open(output, 'w') as file: 
    for keys, value in report.items(): 
        file.write(f" {keys} Values {str(value)}\n")
        
