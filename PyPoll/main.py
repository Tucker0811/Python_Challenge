import csv
import os

# Initialize variables to track the election data
total_votes = 0
candidates = {}
winner = ""
winning_count = 0

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Read the election data
with open(file_to_load, mode='r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip the header

    for row in reader:
        total_votes += 1  # Count total votes
        candidate = row[2]  # Candidate is in the third column

        # Count votes for each candidate
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

# Print total votes
print(f'Total Votes: {total_votes}')

# Print candidates and their vote counts
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    print(f'{candidate}: {percentage:.3f}% ({votes})')

# Determine the winner
winner = max(candidates, key=candidates.get)
print(f'Winner: {winner}')

# Specify the output file path
file_to_output = "output.txt"

# Open the text file to save the output
with open(file_to_output, "w") as txt_file:
    # Print the total vote count (to terminal)
    print(f"Total Votes: {total_votes}")

    # Write the total vote count to the text file
    txt_file.write(f"Total Votes: {total_votes}\n")
    
    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate, votes in candidates.items():
        # Calculate the percentage of votes
        vote_percentage = (votes / total_votes) * 100
        # Print the candidate results to terminal
        print(f"{candidate}: {vote_percentage:.2f}% ({votes})")
        # Write the candidate results to the text file
        txt_file.write(f"{candidate}: {vote_percentage:.2f}% ({votes})\n")
        
        # Determine the winner
        if votes > winning_count:
            winning_count = votes
            winner = candidate

    # Print and write the winner
    print(f"Winner: {winner}")
    txt_file.write(f"Winner: {winner}\n")
    