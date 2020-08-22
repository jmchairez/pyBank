import os
import csv
import numpy as np

bank_csv = os.path.join("..", "Resources", "budget_data.csv")

profit = []
months = []
average_change = []

with open(bank_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)
    #print(f"Header: {csv_header}")
    print("Financial Analysis")
    print("-------------------------")
    
    num_rows = 0
    for rows in csv_reader:
        num_rows += 1 
    
        months.append(rows[0])
        profit.append(int(rows[1]))
    
    for i in range(1, len(profit)):
        average_change.append((int(profit[i]) - int(profit[i-1])))
    




print(f"Total Months: {num_rows}")    
print(f"Total Profit: ${sum(profit)}")   