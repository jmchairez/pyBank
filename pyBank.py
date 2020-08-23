#import the needed libraries
import os
import csv

#set path to csv file
bank_csv = os.path.join("..", "Resources", "budget_data.csv")

#set variables 
profit = []
months = []
average_change = []

#open the csv file budget data, set delimiter, and skip header
with open(bank_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)
    #print(f"Header: {csv_header}")
    print("Financial Analysis")
    print("-------------------------")
    
    #count the total number of rows
    num_rows = 0
    for rows in csv_reader:
        num_rows += 1 
    
        #append to set the totals of profit and months
        months.append(rows[0])
        profit.append(int(rows[1]))
    
    #read throught the data and set profit as integer
    for i in range(1, len(profit)):
        average_change.append((int(profit[i]) - int(profit[i-1])))
    
    #Find the average of the change in "Profit/Losses" over the entire period
    revenue = (round(sum(average_change) / len(average_change), 2))

    #Find the greatest increase and decrease in profit and losses(date and amount) over the entire period
    greatest_increase = max(average_change)
    greatest_decrease = min(average_change)

