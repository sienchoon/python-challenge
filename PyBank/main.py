#importing data from csv files using library module
import os
import csv
from datetime import datetime

#set path to the file
csvpath = os.path.join( "Resources", "budget_data.csv")
print(csvpath)

# Set variable to check if we found the video
found = False

#Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        print(row)




































#Summary of the data analysis
print("\n")
print("Financial Analysis\n")
print("---------------------------------------------------------------\n")

print("Total Months: ")
print("\n")
print("Total: ")
print("\n")
print("Average Change: $")
print("\n")
print("Greatest Increase in Profits:  ")
print("\n")
print("Greatest Decrease in Profits: ")
print("\n")