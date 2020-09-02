import os
import csv

csvpath = os.path.join("Resources", "PyBank.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")

    # grab the header
    header = next(csvreader)
    # determine
    date = []
    profitloss = []
    # add a new list of the change from one row to another
    change = []
     
    # assign each category to appropriate column
    for row in csvreader:
        date.append(str(row[0]))
        profitloss.append(float(row[1]))

    #determine change 
    for c in range(1,len(profitloss)):
        change.append(profitloss[c] - profitloss[c-1])   
        
        # calculate average. identify max & min
        avgchange = sum(change)/len(change)
        maxchange = max(change)
        minchange = min(change)

        # get the date for each max and min
        maxchangedate = str(date[change.index(max(change))])
        minchangedate = str(date[change.index(min(change))])
   
    print("Financial Analysis")
    print("---------------------")    
    print("Total Months: " + str((len((date)))))
    print("Total Revenue: $", sum(profitloss))
    print("Avereage Revenue Change: $", round(avgchange))
    print("Greatest Increase in Revenue:", maxchangedate,"($", maxchange,")")
    print("Greatest Decrease in Revenue:", minchangedate,"($", minchange,")")

    import sys
    with open("PyBank.txt", "w") as outputfile: 
        outputfile.write(f'Total: $ {sum(profitloss)}\n' ) 
        outputfile.write(f'Average Revenue Change: $ {avgchange:,.2F}\n' )
        outputfile.write(f'Greatest Increase in Revenue: {maxchangedate,"($", maxchange,")"}\n' ) 
        outputfile.write(f'Greatest Decrease in Revenue: {minchangedate, "($", minchange,")"}\n' )