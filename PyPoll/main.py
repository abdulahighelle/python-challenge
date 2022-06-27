import os
import csv

ID_Count = 0
Stockham = []
DeGette = []
Doane = []
Candidates = [{"Candidate": "Charles Casper Stockham", "Votes" : f'({len(Stockham)})'},
{"Candidate": "Diana DeGette", "Votes" : f'({len(DeGette)})'},
{"Candidate": "Raymon Anthony Doane", "Votes" : f'({len(Doane)})'},]


csvpath = os.path.join("Resources", "election_data.csv")

with open(csvpath, encoding='utf') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    next(csv_reader)

    for row in csv_reader:
        ID_Count = ID_Count + 1
        if row[2] == "Charles Casper Stockham":
            Stockham.append(row[0])
        if row[2] == "Diana DeGette":
            DeGette.append(row[0])
        if row[2] == "Raymon Anthony Doane":
            Doane.append(row[0])

Stockham_p = (len(Stockham) / ID_Count) *100
DeGette_p = (len(DeGette) / ID_Count) * 100
Doane_p = (len(Doane) / ID_Count) * 100

#The total number of votes cast

print(f'Election Results:\n------------\n Total Votes: {ID_Count}')

#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won

print(f'Charles Casper Stockham: {format(Stockham_p,".3f")}\% ({len(Stockham)}) \n Diana DeGette: {format(DeGette_p,".3f")}\% ({len(DeGette)}) \n Raymon Anthony Doane:  {format(Doane_p,".3f")}\% ({len(Doane)})')

#The winner of the election based on popular vote.

if len(Stockham) > len(DeGette) and len(Stockham) > len(Doane):
    print(f'Winner: {Candidates[0]["Candidate"]}')
if len(DeGette) > len(Stockham) and len(DeGette) > len(Doane):
    print(f'Winner: {Candidates[1]["Candidate"]}')
if len(Doane) > len(DeGette) and len(Doane) > len(Stockham):
    print(f'Winner: {Candidates[2]["Candidate"]}')

#print the analysis to the terminal and export a text file with the results.
with open("PyPoll_Output.txt","w") as text_file:
    text_file.write(f'Election Results:\n------------\nTotal Votes: {ID_Count}')
    text_file.write(f'\nCharles Casper Stockham: {format(Stockham_p,".3f")}% ({len(Stockham)}) \nDiana DeGette: {format(DeGette_p,".3f")}% ({len(DeGette)}) \nRaymon Anthony Doane:  {format(Doane_p,".3f")}% ({len(Doane)})')
    if len(Stockham) > len(DeGette) and len(Stockham) > len(Doane):
        text_file.write(f'\nWinner: {Candidates[0]["Candidate"]}')
    if len(DeGette) > len(Stockham) and len(DeGette) > len(Doane):
        text_file.write(f'\nWinner: {Candidates[1]["Candidate"]}')
    if len(Doane) > len(DeGette) and len(Doane) > len(Stockham):
        text_file.write(f'\nWinner: {Candidates[2]["Candidate"]}')