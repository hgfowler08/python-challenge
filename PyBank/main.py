#Analyze financial data
#Data set is made up of 41 entries, spans over 4 years and contains revenue information
#Import data set
import os
import csv



file = 'budget_data.csv'
#Create path to collect data from the folder
#budgetCSV = os.path.join('..\\Desktop\\budget_data.csv')

#Hold values for variables
date = []
revenue = []

#Read in CSV file
with open(file, 'r') as f:
    csvreader = csv.reader(f, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        date.append(row[0])
        revenue.append(row[1])
    
    #Find total number of months
    totalMonths = len(date)

#Define function and set the financial data as its parameter
#def getFinancial(finData):



#Find total number of months in data set
    #totalMonths = []
    #month = os.listdir(budgetCSV)
    #for month in month:
        #if month.endswith("budget_data.csv"):
            #totalMonths.append(month)
#Find net profit/loss over the time period
    netRev = int()
    for x in range(len(revenue)):
        revenue[x] = int(revenue[x])
        netRev += revenue[x]
#Find average change in profit/loss between months over the total period
    totalChange = int()
    for x in range(len(revenue) - 1):
        totalChange += (revenue[x+1] - revenue[x])
    
    
#Find greatest increase in profits (date and amount) over total period
    greatestincrease = int()
    for x in range(len(revenue)):
        revenue[x] = int(revenue[x])
        greatestincrease = revenue[x] + revenue[x]
    

#Find greatest decreases in losses (date and amount) over total period
    greatestdecrease = int()
    for x in range(len(revenue)):
        revenue[x] = int(revenue[x])
        greatestdecrease = revenue[x] - revenue[x]


print("Total Months:" + str(totalMonths))
print("Total:" + str(netRev))
print("Average Change:" + str(totalChange))
print("Greatest Increase in Profits:" + str(date) + str(greatestincrease))
print("Greatest Decrease in Profits:" + str(date) + str(greatestdecrease))

output = "pybank.csv"

with open('output','w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    writer.writerow(["Financial Analysis"])
    writer.writerow(["---------------------------"])
    writer.writerow(["Total Months:" + str(totalMonths)])
    writer.writerow(["Total:" + str(netRev)])
    writer.writerow(["Average Change:" + str(totalChange)])
    writer.writerow(["Greatest Increase in Profits:" + str(date) + str(greatestincrease)])
    writer.writerow(["Greatest Decrease in Profits:" + str(date) + str(greatestdecrease)])

