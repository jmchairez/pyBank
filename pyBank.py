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

#Print the final script
print(f"Total Months: {num_rows}")    
print(f"Total Profit: ${sum(profit)}")
print(f"Average Change: ${revenue}")
print(f"Greatest Increase in Profits: {str(months[average_change.index(max(average_change))+1])} ${str(greatest_increase)}")
print(f"Greatest Decrease in Profits: {str(months[average_change.index(min(average_change))+1])} ${str(greatest_decrease)}")

#export resutls to a text file
file = open("results_pyBank", "w")

file.write("Financial Analysis")
file.write("\n-------------------------")
file.write(f"\nTotal Months: {num_rows}")    
file.write(f"\nTotal Profit: ${sum(profit)}")
file.write(f"\nAverage Change: ${revenue}")
file.write(f"\nGreatest Increase in Profits: {str(months[average_change.index(max(average_change))+1])} ${str(greatest_increase)}")
file.write(f"\nGreatest Decrease in Profits: {str(months[average_change.index(min(average_change))+1])} ${str(greatest_decrease)}")

file.close()