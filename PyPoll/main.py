#importing data from csv files using library module
import os
import csv


#set path to the file
csvpath = os.path.join( "Resources", "election_data.csv")

with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)