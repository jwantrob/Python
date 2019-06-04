#import modules

import os
import csv

#import csv

csvpath = os.path.join('budget_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    #print(csvreader)

    #print header information
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    #start a total_gain_loss variable = 0
    #start a total month variable = 0
    #create lists to hold gain/loss and date from csv
    total_gain_loss = 0
    total_month = 0
    list_gain_loss = []
    list_date = []
    #add monthly_gain_loss value in each row to total_gain_loss
    #add 1 to each row to get total months (each row = 1 month of data)
    
    for row in csvreader:
        monthly_gain_loss = int(row[1])
        total_gain_loss = total_gain_loss + monthly_gain_loss
        total_month = total_month + 1
        #create lists for gain_loss and dates to iterate through for average and min/max
        list_gain_loss.append(row[1])
        list_date.append(row[0])
#Print Total losses/gains and total months
print('Financial Analysis')
print('--------------------')
print(f'Total Months: {total_month}')
print(f'Total: ${total_gain_loss}')

#create a variable to hold monthly change
total_change = 0
#create a dictionary to hold date and monthly change
date_monthly_change = {}

#compare items in gain_loss list and list_date to find average change and greatest/least profit. Remember list index starts at 0.
for i in range(1,len(list_gain_loss)):
    monthly_change = int(list_gain_loss[i]) - int(list_gain_loss[i-1])
    total_change = total_change + monthly_change
    #append to dictionary the monthly change by date calculated above.
    date_monthly_change.update({list_date[i] : monthly_change})
    #print(date_monthly_change)
#create average monthly change by taking total change and dividing by length of list_gain_loss-1 (since we subtracted the values there is 1 less to divide from)
average_change = total_change/(len(list_gain_loss)-1)
#round to 2 decimal places
round_average_change = round(average_change,2)
print(f'Average Change: ${round_average_change}')
#find the min and max in dictionary date_monthly_change used: http://www.trytoprogram.com/python-programming/python-dictionary/#maxmin
#monthly_max_date = max(date_monthly_change.keys(), key=(lambda a:date_monthly_change[a]))
#.get looks for the largest or smallest value and returns the key in the dictionary used: https://stackoverflow.com/questions/26871866/print-highest-value-in-dict-with-key
monthly_max_date = max(date_monthly_change, key=date_monthly_change.get)
#print(f'max_date: {max_date}')
#max_val = date_monthly_change[max_date]
#print(f'max_val: {max_val}')
#monthly_max_date_test = max(date_monthly_change, key = (lambda a: date_monthly_change[a]))
#print(monthly_max_date_test)
#then you can use that key to return the max/min value
monthly_max_value = date_monthly_change[monthly_max_date]
print(f'Greatest Increase in Profits: {monthly_max_date} (${monthly_max_value})')
#monthly_min_date = min(date_monthly_change.keys(), key=(lambda a: date_monthly_change[a]))
monthly_min_date = min(date_monthly_change, key = date_monthly_change.get)
monthly_min_value = date_monthly_change[monthly_min_date]
print(f'Greatest Decrease in Profits: {monthly_min_date} (${monthly_min_value})')

#Write and print results to .txt file

output_path = os.path.join('Pybank_Results.txt')

with open(output_path, 'w') as txtfile:
    txtfile.write('Financial Analysis\n')
    txtfile.write('--------------------\n')
    txtfile.write(f'Total Months: {total_month}\n')
    txtfile.write(f'Total: ${total_gain_loss}\n')
    txtfile.write(f'Greatest Increase in Profits: {monthly_max_date} (${monthly_max_value})\n')
    txtfile.write(f'Greatest Decrease in Profits: {monthly_min_date} (${monthly_min_value})\n')
print('complete')
        

       

    