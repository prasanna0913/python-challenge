import os 
import csv

#path to csvfile
csvpath = os.path.join('Resources', 'election_data.csv')
print(csvpath)

#Reading the CSV file
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")


    Total_votes = 0
    candidate_list = []
    candidate_vote_count = []

#sniffer is used when header is included in the csv list. sniffer function counts the rows after the header.
    if csv.Sniffer().has_header:
        next(csvreader)
    for row in csvreader:
#Calculating total number of votes:       
        Total_votes = Total_votes + 1

#read list of candidates from column 3 in the csv:
#identify the candidate_name in candidate_list, if not present add +1 to the candidate_vote_count,
#else append the name to candidate_list and add +1 to candidate_vote_count.
        candidate_name = (row[2])
        if candidate_name in candidate_list:
            candidate_index = candidate_list.index(candidate_name)
            candidate_vote_count[candidate_index] = candidate_vote_count[candidate_index] + 1
        else:
            candidate_list.append(candidate_name)
            candidate_vote_count.append(1)


# print(f'Total votes: {Total_votes}')
# print(f'Each candidate: {candidate_list}')
# print(f'Index: {candidate_list.index(candidate_name)}')


percentage = []
highest_count = max(candidate_vote_count)
max_count_index = candidate_vote_count.index(max(candidate_vote_count))
max_count_name = candidate_list[max_count_index]

# print(max_count_name)
# print(max_count_index)
# print(highest_count)
# print(candidate_vote_count)

#Percentage of votes each candidate received:
for x in range(len(candidate_list)):
    vote_percentage = round(candidate_vote_count[x]/Total_votes*100, 2)
    percentage.append(vote_percentage)
    
  
#writing the CSV file to output as text file:  
output_path = os.path.join('Analysis', 'output_election_data.txt')


total = zip(candidate_list, percentage, candidate_vote_count)

with open(output_path, 'w') as outtextfile:
    csvwriter = csv.writer(outtextfile, delimiter = " ")
    

    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["-----------------------"])
    csvwriter.writerows(total)
    csvwriter.writerow(["-----------------------"])
    csvwriter.writerow(["Winner : Khan"])


#print to terminal
print("Election results")
print("-----------------------")
print(f'Total votes: {Total_votes}')
print("------------------------")
print(f'{candidate_list[0]} : {percentage[0]}% ({candidate_vote_count[0]})')
print(f'{candidate_list[1]} : {percentage[1]}% ({candidate_vote_count[1]})')
print(f'{candidate_list[2]} : {percentage[2]}% ({candidate_vote_count[2]})')
print(f'{candidate_list[3]} : {percentage[3]}% ({candidate_vote_count[3]})')
# print(percentage) 
print("----------------------")
print(f'Winner: {max_count_name}')

# print to text file
