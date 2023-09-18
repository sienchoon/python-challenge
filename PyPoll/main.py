#importing data from csv files using library module
import os
import csv

#set path to the file
csvpath = os.path.join("resource", "election_data.csv")

with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    