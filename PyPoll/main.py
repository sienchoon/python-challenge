#importing data from csv files using library module
import os
import csv

#set path to the file
csvpath = os.path.join("resource", "election_data.csv")

total_votes = 0
#list of names of the candidates
candidate_choices = []
#storing the number of votes for each candidates
candidate_votes = []
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

        #incrementing the number of votes for each candidate
        #if candidate name is same, increment by 1
        if row[2] not in candidate_choices:
            #adding the candidate name into the empty list (candidate_choices)
            #if the name is not in the list, the name will be added to the list
            candidate_choices.append(row[2])
            #adding the number into the candidate votes for each similar candidate
            candidate_votes.append(1)
            #finding the index of candidate's name in row[2]
            index = candidate_choices.index(row[2])
            #incrementing the vote count for the candidate's vote
            candidate_votes[index] += 1 
        else:
            index = candidate_choices.index(row[2])
            candidate_votes[index] += 1
                   
#finding the % of votes for each candidate got
    for votes in candidate_votes:
        percentage = (votes/total_votes) * 100
        formatted_percentage = "{:.2f}".format(percentage)
        percentage_votes.append(formatted_percentage)

#finalising the summary of the election    
winning_candidate = max(candidate_votes)
index = candidate_votes.index(winning_candidate)
winner = candidate_choices[index]    
  
#Summary of the data analysis on the terminal:
print("\n")
print("Election Results\n")
print("---------------------------------------------------------------\n")
#str to convert to string
print(f"Total Votes: {str(total_votes)}\n")
print("---------------------------------------------------------------\n")
for i in range(len(candidate_choices)):
    print(f"{candidate_choices[i]}: {str(percentage_votes[i])}% ({str(candidate_votes[i])})\n")
print("---------------------------------------------------------------\n")
print(f"Winner: {winner}\n")

#exporting to analysis folder and creating a summary.txt
file_output_name = "summary.txt"
output_folder = "analysis"
file_path = os.path.join(output_folder, file_output_name)
#printing/exporting the results as a text file:
with open(file_path, "w") as text:
#loop through lines to export
    text.write(f'Election Results\n')
    text.write(f'---------------------------------------------------------------\n')
    text.write(f'Total Votes: {str(total_votes)}\n')
    text.write(f'---------------------------------------------------------------\n')
    for i in range(len(candidate_choices)):
        text.write(f'{candidate_choices[i]}: {str(percentage_votes[i])}% ({str(candidate_votes[i])})\n')
    text.write(f'---------------------------------------------------------------\n')
    text.write(f'Winner: {winner}\n')

print(f"The summary has been saved as {file_output_name} and exported to {file_path}.")