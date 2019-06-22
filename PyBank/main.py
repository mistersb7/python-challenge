import os

import csv

import subprocess

total = 0
rownum= 0
changeavgtot= 0

months= []
profit= []
amtchange= []

csvpath = os.path.join('budget_data.csv')


with open(csvpath, newline='') as csvfile:
    csvreader= csv.reader(csvfile, delimiter=',')    
    csv_header = next(csvreader)
      
    for row in csvreader:
        months.append(row[0])
        profit.append(row[1])
        total = total + int(row[1])
        change = int(profit[rownum]) - int(profit[rownum - 1])
        amtchange.append(change)
        changeavgtot += change
        rownum += 1


avgchange = changeavgtot / (len(amtchange)-1)

lowestprofit= min(amtchange)

highestprofit= max(amtchange)

lowestindex= amtchange.index(lowestprofit)

lowestmonth = months[lowestindex]

highestindex= amtchange.index(highestprofit)

highestmonth= months[highestindex]



print("Financial Analysis")
print("----------------------------")
print(f"Total Months:", len(months))
print(f"Total: $", total)
print(f"Average Change: $", round(avgchange,2))
print(f"Greatest Increase in Profits: {highestmonth} (${highestprofit})")
print(f"Greatest Decrease in Profits: {lowestmonth} (${lowestprofit})" )



txt_file= open("Output.txt", 'w', newline='')
txt_file.write("Financial Analysis\n")
txt_file.write("----------------------------\n")
txt_file.write(f"Total Months: {len(months)}\n")
txt_file.write(f"Total: ${total}\n")
txt_file.write(f"Average Change: ${round(avgchange,2)}\n")
txt_file.write(f"Greatest Increase in Profits: {highestmonth} (${highestprofit})\n")
txt_file.write(f"Greatest Decrease in Profits: {lowestmonth} (${lowestprofit})\n" )
txt_file.close()

#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The average of the changes in "Profit/Losses" over the entire period
##The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period


#As an example, your analysis should look similar to the one below:


  #Financial Analysis
  # ----------------------------
 # Total Months: 86
  #Total: $38382578
  #Average  Change: $-2315.12
 # Greatest Increase in Profits: Feb-2012 ($1926159)
 # Greatest Decrease in Profits: Sep-2013 ($-2196167)