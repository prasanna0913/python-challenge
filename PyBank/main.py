import os 
import csv


csvpath = os.path.join('Resources', 'budget_data.csv')

print(csvpath)

#Reading the CSV file
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")


#defining the variables
    Total_months=0
    net_profit_loss = 0
    avergae = 0
    allchanges = []
    allmonths = []
    previous_month = 0
    current_month = 0
    profit_loss_change = 0
    
#Sniffer funtion to remove the header in the list and count the remaining rows which gives the total number of rows(months):    
    if csv.Sniffer().has_header:
        next(csvreader)
    #Total number of months in the budget data:
    for row in csvreader:
        Total_months = Total_months + 1

        # calculating Net profit loss
        current_month = int(row[1])
        net_profit_loss += current_month

        if (Total_months == 1):
            # set value for first record
            previous_month = current_month
        else:

            # change in profit loss 
            profit_loss_change = current_month - previous_month

            # Append all months[]
            allmonths.append(row[0])

            # Append all changes[]
            allchanges.append(profit_loss_change)

            # reset value to previous month
            previous_month = current_month

    #calculating total sum and average
    Totalsum = sum(allchanges)
    Average = round(Totalsum/(Total_months - 1), 2)


    # minimum and maximum values for profit and loss
    maximum = max(allchanges)
    minimum = min(allchanges)

    # index of min and max 
    max_index = allchanges.index(maximum)
    min_index = allchanges.index(minimum)


    # best and worst month
    best_month = allmonths[max_index]
    worst_month = allmonths[min_index]

#print to terminal
print("Financial Analysis")   
print("--------------------------")
print(f"Total_months: {Total_months}")
print (f"Total: {net_profit_loss}")
print (f"Average Change: {Average}")
print (f"Greatest increase in profits:  {best_month} {maximum}")
print (f"Greatest decrease in profits:  {worst_month} {minimum}")

#defining the variables
index = []
index = [1,2,3,4,5]
average_change = str('($ ') + str(Average) + str(' )')
bestmax = str(best_month) + str(' : ') + str('($ ') + str(maximum) + str(' )')
worstmin = str(worst_month) + str(' : ') + str('($') + str(minimum) + str(' )')

result = [Total_months,net_profit_loss,average_change,bestmax,worstmin]
col_header = ["Total_months", "Total", "Average Change", "Greatest increase in profits", "Greatest decrease in profits"]

data = zip(index, col_header, result)
print(data)

# writing the csv file as output to text file
output_path = os.path.join('Analysis', 'budget_output.txt')

with open(output_path, 'w') as outcsvfile:
    csvwriter = csv.writer(outcsvfile, delimiter = " ")
    
    #write to the text file
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["-----------------------"])
    csvwriter.writerows(data)
