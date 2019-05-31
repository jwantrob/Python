#import modules

import os
import csv

#import csv

csvpath = os.path.join('election_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    print(csvreader)

    #print header information
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    
    #start a total_vote variable = 0
    total_vote = 0
    #start a blank candidate_list for all rows
    candidate_list_long =[]

    #add 1 to each row to get total votes (each row = 1 vote)
    #make a list of candidates from every row
    for row in csvreader:
        total_vote = total_vote + 1
        candidate_list_long.append(row[2])
#count votes by candidate.  Found help usinng https://stackoverflow.com/questions/2600191/how-can-i-count-the-occurrences-of-a-list-item        
candidate_list = [[x,candidate_list_long.count(x)] for x in set(candidate_list_long)]
print(candidate_list)
#print(len(candidate_list))
#create a vote percent by dividing each total vote by candidate in candidate_list by total_list
for i in range(0,len(candidate_list)):
    vote_percent = round((int(candidate_list[i][1])/total_vote)*100,0)
    #candidate_list_per.append(vote_percent)
    #append this to each nested list
    candidate_list[i].append(vote_percent)
    #print(vote_percent)
#print(candidate_list)
      
#Print Election Results
print('Election Results')
print('--------------------')
print(f'Total Votes: {total_vote}')
print('--------------------')