import os
import csv

bank_csv = os.path.join("..", "Resources", "budget_data.csv")

with open(bank_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    num_rows = 0

    for row in csv_reader:
        num_rows += 1 
    print(num_rows)    
