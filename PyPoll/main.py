import csv
import pandas as pd
import pprint as pp
import time


#  Pandas method  
csv_path = "Resources/election_data.csv"

election_pd = pd.read_csv(csv_path)

total_votes = election_pd.shape[0]


candidates = election_pd['Candidate'].unique()

count_df = election_pd['Candidate'].value_counts()

percent_df = election_pd['Candidate'].value_counts(normalize=True)


print(f"\n------------------------- Pandas Solution ------------------------- \n\
Election Results \n\
------------------------- \n\
Total Votes: {total_votes} \n\
------------------------- ")
for candidate in candidates:
    print(f"{candidate}: {round(percent_df[candidate]*100,3)}% ({count_df[candidate]})")
print(f"------------------------- \n\
Winner: {count_df.idxmax()} \n\
-------------------------") 


#  CSV method  
total_votes = 0

# dict[candidate] = votes
candidates = {}

with open(csv_path, mode="r") as csv_file:
    reader = csv.reader(csv_file, delimiter=",")
    next(reader, None)
    for row in reader:
        candidate = row[2]
        
        # Count up total votes
        total_votes = total_votes + 1

        # if inside the dict, votes +1 (value of dict entry) 
        if candidate in candidates.keys():
            candidates[candidate] += 1
        
        # if not inside the dict, add a new entry to the dict and set votes to 1
        else:
            candidates[candidate] = 1
    
print(f"\n------------------------- CSV Solution ------------------------- \n\
Election Results \n\
------------------------- \n\
Total Votes: {total_votes} \n\
------------------------- ")
# print out each candidates stats
for candidate in candidates.keys():
    votes = candidates[candidate]
    percent_votes = "%0.3f" % (( votes / total_votes)* 100) 
    print(f"{candidate}: {percent_votes}% ({votes})")

print(f"------------------------- \n\
Winner: {max(candidates, key=candidates.get)} \n\
-------------------------") 
