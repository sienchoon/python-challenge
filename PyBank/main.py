#importing data from csv files using library module
import os
import csv

#set path to the file
csvpath = os.path.join( "Resources", "budget_data.csv")
print(csvpath)

#create a loop to go through each row of data
#initialise variables to start the count
#value starts with 0 to keep track of the changes
total_months = 0
total_profit = 0

#value is the profit/loss of the month and located at row[1]
initial_value = 0 
change = 0

#putting the date and profits in list
#put the list in a loop to find the index of the greatest increase and decrease
dates = []
profits = []

#Open the CSV using the UTF-8 encoding
#conditions and initialising the variables to start the count
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #separating the header
    #the data contains header, so we need to skip it
    header = next(csvfile)     
#in csv file, date and profit/loss are in row[0] and row[1] 
    for row in csvreader:
        #dates are put into a list, row[0] indicates the location of the data in the csv file
        dates.append(row[0])
        
        # finding the change in profits
        change = int(row[1]) - initial_value
        profits.append(change)
        initial_value = int(row[1])

        #using increment to keep count of the months and total profit
        total_months += 1
        total_profit = total_profit + int(row[1])


# finding greates increase in profits
# using max to find the greatest increase
# using index to find the date
greatest_increase = max(profits)
best_index = profits.index(greatest_increase)
best_date = dates[best_index]


#finding greates decrease in profits
#using min to find the greatest decrease
#using index to find the date
greatest_decrease = min(profits)
worst_index = profits.index(greatest_decrease)
worst_date = dates[worst_index]

#finding the average change
average_change = sum(profits)/len(profits)

#formatting the average change to 2 decimal places
formatted_average_change = "{:.2f}".format(average_change)

#Summary of the data analysis on the terminal:
print("\n")
print("Financial Analysis\n")
print("---------------------------------------------------------------\n")
#str to convert to string
print(f"Total Months: {str(total_months)}\n")
print(f"Total: ${str(total_profit)}\n")
print(f"Average Change: ${str(formatted_average_change)}\n")
print(f"Greatest Increase in Profits: {best_date} : ${str(greatest_increase)}\n") 
print(f"Greatest Decrease in Profits: {worst_date} : ${str(greatest_decrease)}\n")



#formatting the lines in a list
lines_to_export = [   
    "Financial Analysis\n",
    "---------------------------------------------------------------\n",
    f"Total Months: {str(total_months)}\n",
    f"Total: ${str(total_profit)}\n",
    f"Average Change: ${str(formatted_average_change)}\n",
    f"Greatest Increase in Profits: {best_date} : ${str(greatest_increase)}\n",
    f"Greatest Decrease in Profits: {worst_date} : ${str(greatest_decrease)}\n",
]

#printing/exporting the results as a text file:
with open("output.txt", "w") as text:
#loop through lines to export
    for line in lines_to_export:
        text.write(line)

print("The summary has been exported to output.txt")