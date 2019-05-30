#import modules

import os
import csv

#import csv

csvpath = os.path.join('PyBank','budget_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    print(csvreader)

    #print header information
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    #start a total_gain_loss variable = 0
    #start a total month variable = 0
    total_gain_loss = 0
    total_month = 0

    #add second column value in each row to total_gain_loss
    #add 1 to each row to get total months (each row = 1 month of data)
    for row in csvreader:
        total_gain_loss = total_gain_loss + int(row[1])
        total_month = total_month + 1
    #Print Total losses/gains and total months
    print(f'Total Months: {total_month}')
    print(f'Total: ${total_gain_loss}')
    