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
    #add 1 to each row to get total votes (each row = 1 vote)
    
    for row in csvreader:
        total_vote = total_vote + 1
#Print Total losses/gains and total months
print('Election Results')
print('--------------------')
print(f'Total Votes: {total_vote}')
print('--------------------')