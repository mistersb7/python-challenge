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

txt_file= open("Output.txt", 'w', newline='')
txt_file.write(f"\n")
txt_file.write(f"Candidates who received votes: {ucandidate}\n")
txt_file.write(f"\n")
txt_file.write(f"Election Results\n")
txt_file.write(f"-------------------------\n")
txt_file.write(f"Total votes: {len(totalvotes)}\n")
txt_file.write(f'-------------------------\n')
txt_file.write(f"Khan: {khanpercent}% ({len(khanvotes)})\n")
txt_file.write(f"Correy: {correypercent}% ({len(correyvotes)})\n")
txt_file.write(f"Li: {lipercent}% ({len(livotes)})\n")
txt_file.write(f"O'Tooley: {otooleypercent}% ({len(otooleyvotes)})\n")
txt_file.write("-------------------------\n")
txt_file.write(f"Winner:{winner}\n")
txt_file.write("-------------------------\n")
txt_file.close()