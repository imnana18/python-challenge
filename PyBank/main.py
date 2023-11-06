import pandas as pd
import csv 
import time

# Pandas solution
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

csv_path = "Resources/budget_data.csv"

budget = pd.read_csv(csv_path)

Total_month = budget.shape[0]

Total_budget = budget['Profit/Losses'].sum()

Average_Change = "%0.2f" % budget['Profit/Losses'].mean()

Greatest_Increase = budget['Profit/Losses'].max()

Greatest_Decrease = budget['Profit/Losses'].min()

max_index = budget['Profit/Losses'].idxmax()
min_index = budget['Profit/Losses'].idxmin()

print("\n----------------- Pandas Solution -----------------\n")
print(f" Financial Analysis \n\
---------------------------- \n\
Total Months: {Total_month} \n\
Total: $ {Total_budget} \n\
Average Change: $ {Average_Change} \n\
Greatest Increase in Profits: {budget.iloc[max_index,0]} (${Greatest_Increase}) \n\
Greatest Decrease in Profits: {budget.iloc[min_index,0]} (${Greatest_Decrease})")

# csv solution
total_months = 0
total = 0
average_change = 0
greatest_increase = 0
greatest_decrease = 0
greatest_increase_month = 0
greatest_decrease_month = 0

with open(csv_path, newline="") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    next(reader, None)
    for row in reader:
        month = row[0]
        profit = int(row[1])

        # One month per row
        total_months = total_months + 1

        # Aggregate profit per row
        total = total + profit

        # Check if profit is greater than the max if so update the record of max
        if profit > greatest_increase :
            greatest_increase = profit
            greatest_increase_month = month
        
        # Vice versa
        if profit < greatest_decrease:
            greatest_decrease = profit
            greatest_decrease_month = month
    
    # Simply calculate average
    average_change = "%0.2f" % (total / total_months)

print("\n----------------- CSV Solution -----------------\n")
print(f" Financial Analysis \n\
---------------------------- \n\
Total Months: {total_months} \n\
Total: $ {total} \n\
Average Change: $ {average_change} \n\
Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase}) \n\
Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")