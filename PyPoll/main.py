import os
import csv

# my variables
votes_total = 0
candidates = {}
votes_winners = 0
percentage = {}

#path
csvpath = os.path.join('C:/Users/Vanessa/Desktop/2022 Bootcamp/Home Work/Python-Challenge-/PyPoll/Resources/election_data.csv') 

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvfile)

    for row in csvreader:

        votes_total = votes_total + 1

        if row[2] in candidates:
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1



for key, value in candidates.items():
    percentage[key] =round((value/votes_total)* 100 , 3)


    if percentage[key] > votes_winners:
        votes_winners = candidates[key]
        winner = key



#my analysis

print(f"Election Results")
print(f"-------------------")
print(f"votes_total: {votes_total}")
print(f"--------------------")
for key, value in candidates.items():
    print(key, ':' , str(percentage[key]),'%',' ','(',candidates[key],')')
print(f"-------------------")
print(f"Winner: {winner}")
print(f"-------------------")

with open("PyPoll.txt", "w") as text:
text.write(f"Election Results")
text.write(f"-------------------")
text.write(f"votes_total: {votes_total}")
text.write(f"--------------------")
for key, value in candidates.items():
    text.write(key, ':' , str(percentage[key]),'%',' ','(',candidates[key],')')
text.write(f"-------------------")
text.write(f"Winner: {winner}")
text.write(f"-------------------")

