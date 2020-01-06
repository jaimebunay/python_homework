# Import the pathlib and csv library
from pathlib import Path
import csv 
import statistics

def difference(a,b): 
    difference = a-b
    return difference

# Set the file path 
#print(f"This is your current working directory: {Path.cwd()}")
#print() 

csv_filepath = Path('Resources/budget_data.csv')


# Initialize variables to hold dates and profits 
profits_n_losses = {}
list_profits = []
list_of_differences =[]
month_count = 0 
total = 0 

with open(csv_filepath, 'r') as csvfile: 
    # Print the datatype of the file object
    #print(type(csv_filepath))
    #print()

    #pass in the csv file to the csv.reader() function
    csv_reader = csv.reader(csvfile, delimiter = ',')

    #print the datatype of the csvreader 
    #print(type(csv_reader))

    # Go to the next row from the start of the file
    # Here we are going to the first row/header of the csvreader file

    header = next(csv_reader)

    
    # Now we will iterate to through the csv_reader file 
    # We will be going through each row of data after the header 

    for row in csv_reader: 
        # Add keys and values to the profit_n_losses dictionary
        profits_n_losses[row[0]] = int(row[1])
        list_profits.append(int(row[1]))
        month_count += 1 
        total += int(row[1])



# Now we will initialize metric values
total_months = 0 
total_profit = 0 
average_change = 0 
greatest_increase = 0
greatest_increase_key =''
greatest_decrease = 0
greatest_decrease_key=''
index = 0

# Now we will do our calculations by using a for loop
for key, value in profits_n_losses.items():
    if index >= 1: 
        diff = difference(int(value), list_profits[index - 1])
        list_of_differences.append(diff)
        if diff > greatest_increase:
            greatest_increase = diff
            greatest_increase_key = key
        if diff < greatest_decrease:
            greatest_decrease = diff
            greatest_decrease_key = key
    index += 1

# In order to do this, I had to import the "statistics" librart 
# https://appdividend.com/2019/01/28/python-statistics-tutorial-mean-function-example/
average_change = round(statistics.mean(list_of_differences), 2)

print("Financial Analysis")
print('-'*28) 
print(f"Total Months: {month_count}")
print(f"Total: ${total}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_key} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_key} (${greatest_decrease})")

output_path = Path("financial_analysis_results.txt")

with open(output_path, 'w') as file: 
    file.write("Financial Analysis\n")
    file.write('-'*28) 
    file.write(f"\nTotal Months: {month_count}")
    file.write(f"Total: ${total}\n")
    file.write(f"Average Change: ${average_change}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase_key} (${greatest_increase})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease_key} (${greatest_decrease})\n")


