#importing data from csv files using library module
import os
import csv

#set path to the file
csvpath = os.path.join("resource", "election_data.csv")

total_votes = 0
#list of names of the candidates
candidate_choices = []
#number of votes for each candidates
candidate_votes = {}
#list of percentage of votes for each candidate
percentage_votes = []
#winner of the election
winner = " "


with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvfile)
    
    for row in csvreader:
        #incrementing the total votes to find total_votes
        total_votes += 1        
        #location of candidates in csv file
        candidate_name = row[2]
       
        #incrementing the number of votes for each candidate
        #if candidate name is same, increment by 1
        if candidate_name not in candidate_choices:
           candidate_choices.append(candidate_name)
           candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1
        
#finding the % of votes for each candidate got
    # for votes in num_votes:
    #     percentage = (votes/total_votes) * 100
    #     formatted_percentage = "{:.3f}".format(percentage)
    #     percentage_votes.append(formatted_percentage)
    

    
  
#Summary of the data analysis on the terminal:
print("\n")
print("Election Results\n")
print("---------------------------------------------------------------\n")
#str to convert to string
print(f"Total Votes: {str(total_votes)}\n")
print("---------------------------------------------------------------\n")



print("---------------------------------------------------------------\n")
print(f"Winner: {winner}\n")

