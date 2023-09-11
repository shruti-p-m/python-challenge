import os
import csv

#setting path for file
election_csv = os.path.join('Resources', 'election_data.csv')

#intializing lists for ballot id, county, and candiate data
ballot_id = []
county = []
candidate = []

#reading in the csv file
with open(election_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter = ',')
    header = next(csvreader)

    #filling the ballot_id, county, and candiate lists
    for row in csvreader:
        ballot = int(row[0])
        ballot_id.append(ballot)

        a_county = row[1]
        county.append(a_county)

        a_candiate = row[2]
        candidate.append(a_candiate)

print(len(ballot_id))

charles = 0
diana = 0
raymon = 0
for i in range(len(candidate)):
    a_candiate = candidate[i]
    if a_candiate == "Charles Casper Stockham":
        charles = charles + 1
    elif a_candiate == "Diana DeGette":
        diana = diana + 1
    elif a_candiate == "Raymon Anthony Doana":
        raymon = raymon + 1

print(charles)