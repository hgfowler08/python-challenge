#Analyze voter data
import os
import csv



#Create path to collect data from the folder
pollCSV = os.path.join('..', 'Resources', 'election_data.csv')
#Define function
def getPercentages(pollData):

#Find total amount of votes cast
    totalVotes = str(pollData[1])
#List of all candidates

#% of votes each candidate won

#total number of votes each candidate won

#Winner based on popular vote


#Print values
print("Total Votes:" + str(totalVotes))


# Read in the CSV file
with open(pollCSV, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)