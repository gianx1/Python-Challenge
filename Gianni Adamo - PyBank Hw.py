import os
import csv

budget_data_csv_path = ("budget_data.csv")

with open (budget_data_csv_path) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=",")
    first_row = next(csvreader)
    print(first_row)