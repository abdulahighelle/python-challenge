import csv
import os

months = []
ProfLoss = 0
Increase = 0
Decrease = 0

csvpath = os.path.join("Resources" ,"budget_data.csv")

with open(csvpath, encoding='utf') as csvfile:
    
    csv_reader = csv.reader(csvfile, delimiter=',')
    
    next(csv_reader)
    
    for row in csv_reader:
        months.append(row[0])
        ProfLoss = ProfLoss + int(row[1])
        if int(row[1]) > Increase:
            Increase = int(row[1])
            Largest = row[0]
        if int(row[1]) < Decrease:
            Decrease = int(row[1])
            Smallest = row[0]


Average = ProfLoss / len(months)


print(f' Total Months: {len(months)} \n Total: {ProfLoss} \n Average Change: {Average}')
print(f' Greatest Increase in Profits: {Largest} ({Increase})\n Greatest Decrease in Profits: {Smallest} ({Decrease})')

with open("PyBank_Output.txt","w") as text_file:
    text_file.write(f' Total Months: {len(months)} \n Total: {ProfLoss} \n Average Change: {Average}')
    text_file.write(f' Greatest Increase in Profits: {Largest} ({Increase})\n Greatest Decrease in Profits: {Smallest} ({Decrease})')

#Total Number of Months in Data
#Net Total P&L over entire period
#Average change in profits
#Greatest Increase - Period and amount
#Greatest Decrease - Period and amount

#Print to terminal and create txt file with results