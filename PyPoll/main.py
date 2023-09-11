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

#calculating total number of votes
total_votes = len(ballot_id)

#intializing variable to keep track of how many votes each candiate got
charles = 0
diana = 0
raymon = 0

#counting who got what number of votes
for i in range(len(candidate)):
    a_candiate = candidate[i]
    if a_candiate == "Charles Casper Stockham":
        charles = charles + 1
    elif a_candiate == "Diana DeGette":
        diana = diana + 1
    elif a_candiate == "Raymon Anthony Doane":
        raymon = raymon + 1

#calculating what percentage of the votes each candiate got, and rounding the number to the third decimal place
charles_percent = round(charles / len(candidate) * 100, 3)
diana_percent = round(diana / len(candidate) * 100, 3)
raymon_percent = round(raymon / len(candidate) * 100, 3)

#calculating the winner based on the percentage
if charles_percent > raymon_percent:
    if charles_percent > diana_percent:
        winner = "Charles Casper Stockham"
    else:
        winner = "Diana DeGette"
else:
    if raymon_percent > diana_percent:
        winner = "Raymon Anthony Doane"
    else:
        winner = "Diana DeGette"


#printing election results to the terminal
print('Election Results')
print('-------------------------')
print(f'Total Votes: {total_votes}')
print('-------------------------')
print(f'Charles Casper Stockham: {charles_percent}% ({charles})')
print(f'Diana DeGette: {diana_percent}% ({diana})')
print(f'Raymon Anthony Doane: {raymon_percent}% ({raymon})')
print('-------------------------')
print(f'Winner: {winner}')
print('-------------------------')

#setting path for analysis file
analysis_txt = os.path.join('analysis', 'analysis.txt')

#opening analysis file and printing Election Results to the file, which is what file = text does
#https://stackoverflow.com/questions/36571560/directing-print-output-to-a-txt-file
with open(analysis_txt, 'w') as text:
    print('Election Results', file = text)
    print('-------------------------', file = text)
    print(f'Total Votes: {total_votes}', file = text)
    print('-------------------------', file = text)
    print(f'Charles Casper Stockham: {charles_percent}% ({charles})', file = text)
    print(f'Diana DeGette: {diana_percent}% ({diana})', file = text)
    print(f'Raymon Anthony Doane: {raymon_percent}% ({raymon})', file = text)
    print('-------------------------', file = text)
    print(f'Winner: {winner}', file = text)
    print('-------------------------', file = text)