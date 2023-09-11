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

#round average change to typical ##.## format
#https://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points
rounded_average_change = round(average_change, 2)

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

#printing Financial Analysis to terminal
print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {total_months}')
print(f'Total: ${total_profit_losses}')
print(f'Average Change: ${rounded_average_change}')
print(f'Greatest Increase in Profits: {change_date[index_increase]} (${greatest_increase})')
print(f'Greatest Decrease in Profits: {change_date[index_decrease]} (${greatest_decrease})')

#setting path for analysis file
analysis_txt = os.path.join('Analysis', 'analysis.txt')

#opening analysis file and printing Finacial Analysis to the file, which is what file = text does
#https://stackoverflow.com/questions/36571560/directing-print-output-to-a-txt-file
with open(analysis_txt, 'w') as text:
    print('Financial Analysis', file = text)
    print('----------------------------', file = text)
    print(f'Total Months: {total_months}', file = text)
    print(f'Total: ${total_profit_losses}', file = text)
    print(f'Average Change: ${rounded_average_change}', file = text)
    print(f'Greatest Increase in Profits: {change_date[index_increase]} (${greatest_increase})', file = text)
    print(f'Greatest Decrease in Profits: {change_date[index_decrease]} (${greatest_decrease})', file = text)
