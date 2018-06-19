#Analyze voter data
#import os
import csv


file = 'C:\\Users\\hgfow\\Desktop\\election_data.csv'

#Hold values for variables
voter = [0]
county = [0]
candidate = [0]
#Create path to collect data from the folder
#pollCSV = os.path.join('..', 'Resources', 'election_data.csv')
#Define function
#def getPercentages(pollData):

# Read in the CSV file
with open('election_data.csv', 'r') as f:

    # Split the data on commas
    csvreader = csv.reader(f, delimiter=',')

    header = next(csvreader)

    for row in csvreader:
        voter.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

#Find total amount of votes cast
        voter = len(row[0])    
#List of all candidates

#% of votes each candidate won

#total number of votes each candidate won

#Winner based on popular vote


#Print values
print("Total Votes:" + str(voter))


