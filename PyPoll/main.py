import os

import csv

totalvotes= []
khanvotes= []
correyvotes=[]
livotes=[]
otooleyvotes=[]

csvpath = os.path.join('election_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader= csv.reader(csvfile, delimiter=',')    
    csv_header = next(csvreader)

    for row in csvreader:
        totalvotes.append(row[2])

        

    for candidate in totalvotes:
        if candidate == "Khan":
            khanvotes.append(candidate)
        elif candidate == "Correy":
            correyvotes.append(candidate)
        elif candidate == "Li":
            livotes.append(candidate)
        elif candidate == "O'Tooley":
            otooleyvotes.append(candidate)

khanpercent= round((len(khanvotes) / len(totalvotes)) * 100, 4)
correypercent= round((len(correyvotes) / len(totalvotes)) * 100, 4)
lipercent= round((len(livotes) / len(totalvotes)) * 100, 4)
otooleypercent= round((len(otooleyvotes) / len(totalvotes)) * 100, 4)

ucandidate= set(totalvotes)
winner = max(set(totalvotes),key=totalvotes.count)    

print(f"")
print(f"Candidates who received votes: {ucandidate}")
print(f"")
print(f"Election Results")
print(f"-------------------------")
print(f"Total votes: {len(totalvotes)}")
print(f'-------------------------')
print(f"Khan: {khanpercent}% ({len(khanvotes)})")
print(f"Correy: {correypercent}% ({len(correyvotes)})")
print(f"Li: {lipercent}% ({len(livotes)})")
print(f"O'Tooley: {otooleypercent}% ({len(otooleyvotes)})")
print("-------------------------")
print(f"Winner:{winner}")
print("-------------------------")



#* In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.)

#* You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:

 # * The total number of votes cast

 # * A complete list of candidates who received votes

 # * The percentage of votes each candidate won

 # * The total number of votes each candidate won

 # * The winner of the election based on popular vote.

#* As an example, your analysis should look similar to the one below:

 # ```text
 # Election Results
 # -------------------------
  #Total Votes: 3521001
 # -------------------------
 # Khan: 63.000% (2218231)
 # Correy: 20.000% (704200)
  #Li: 14.000% (492940)
 # O'Tooley: 3.000% (105630)
  #-------------------------
 # Winner: Khan
 # -------------------------
 # ```