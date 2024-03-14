# import the os module to create file paths across operating systems
import os

# import csv Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

# Initialise variables
total_votes = 0
candidates = {}
winner = ""
winner_votes = 0

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')


    # store the header row first 
    csv_header = next(csvreader)


    # Loop through each row of data
    for row in csvreader:
        
# Count the total number of votes 
        total_votes = total_votes + 1
        
        # Get the candidate's name
        candidate_name = row[2]
        
        # Add candidate to the dictionary if not already present
        if candidate_name not in candidates:
            candidates[candidate_name] = 0
            
        
        # Increment the candidate's vote count
        candidates[candidate_name] =  candidates[candidate_name]+1
     

# Print the analysis results
print("\nElection Results\n")
print("-------------------------\n")
print(f"Total Votes: {total_votes}\n")
print("-------------------------\n")

# loop through the candidates dictionary, calculate and print the results for each candidate
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {round(percentage,3)}% ({votes})\n")
    
    # Check for the winner based on highest number of votes
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes
print("-------------------------\n")
print(f"Winner: {winner}\n")
print("-------------------------\n")

# Write the analysis results to a text file
output_file = os.path.join('analysis', 'election_results.txt')
with open(output_file, 'w') as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        file.write(f"{candidate}: {round(percentage,3)}% ({votes})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")