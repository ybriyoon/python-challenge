import os
import csv
csvpath = os.path.join("Documents", "PyPoll.csv")

with open("PyPoll.csv") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    header = next(csvreader)

    # determine
    totalvotes = []

    for row in csvreader:
        totalvotes.append(str(row[0]))
    
    print("Election Results")
    print("---------------------")    
    print("Total Votes: ", str(len(totalvotes)))
    print("---------------------")

    # no_duplicates = set(tuple(row) for row in csvreader)
    candidates = []
    duplicatecandidates = []
    for line in csvfile:
        columns = line.strip().split(',')
        if columns[2] not in candidates:
           candidates.append(columns[2])
        else: 
           duplicatecandidates.append(columns[2])