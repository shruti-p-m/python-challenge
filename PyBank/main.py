import os
import csv

#setting path for file
budget_csv = os.path.join('Resources','budget_data.csv')

#intializing lists for months and profit/losses
months = []
profit_losses = []

#reading in the csv file
with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter = ',')
    header = next(csvreader)

    #filling the months and profit_losses list
    for row in csvreader:
        month = row[0]
        months.append(month)

        profit = int(row[1])
        profit_losses.append(profit)

#calculating the total months and total profit/losses for the financial analysis
total_months = len(months)
total_profit_losses = sum(profit_losses)

#initializing change list and the corresponing date list
change = []
change_date = []

#creating for loop to fing change in profit between each month, and the month in which the change occured
for i in range(total_months - 1):
    before = profit_losses[i]
    after = profit_losses[i + 1]
    change_data = months[i + 1]
    difference = after - before
    change.append(difference)
    change_date.append(change_data)

#calculating average change
average_change = (sum(change)/len(change))

#initializing variable to find greatest increase and decrease in profit, and the variable to hold the index
greatest_increase = change[0]
greatest_decrease = change[0]
index_increase = 0
index_decrease = 0

#find the greatest increase and decrease, and the index of those values
for i in range(len(change)):
    profit_change = change[i]
    
    # replace greater increase change if current value is bigger, and hold that index
    if profit_change > greatest_increase:
        greatest_increase = profit_change
        index_increase = i
    else:
        "hi"
    # replace greater decrease change if current value is smaller, and hold that index
    if profit_change < greatest_decrease:
        greatest_decrease = profit_change
        index_decrease = i


print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {total_months}')
print(f'Total: ${total_profit_losses}')
print(f'Average Change: ${average_change}')
print(f'Greatest Increase in Profits: {change_date[index_increase]} (${greatest_increase})')
print(f'Greatest Decrease in Profits: {change_date[index_decrease]} (${greatest_decrease})')
