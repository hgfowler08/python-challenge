#Analyze voter data
import os
import csv


#file = "election_data.csv"

#Hold values for variables
ID = [0]
county = [0]
candidate = [0]
#Create path to collect data from the folder
#pollCSV = os.path.join('..', 'Resources', 'election_data.csv')
#Define function
#def getPercentages(pollData):

#Find total amount of votes cast
    #totalVotes = int(pollData[1])
#List of all candidates

#% of votes each candidate won

#total number of votes each candidate won

#Winner based on popular vote


#Print values
#print("Total Votes:" + str(totalVotes))


# Read in the CSV file
with open('election_data.csv', 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    for row in csvreader:
        if row[0] == voter:
            print(voter)
        elif row[1] == county:
            print(county)
        elif row[2] == candidate:
            print(candidate)