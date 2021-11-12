# The data we need to retrieve
# 1.The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

# Add our dependencies
import csv
import os
# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources_EA", "election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1 Initialize a total vote counter
total_votes = 0

# Candidate options and candidate votes
candidate_options = []

# Candidate votes - Declare dictionary
candidate_votes = {}

# Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)  
    # Read the header row
    headers = next(file_reader)
    # Print each row in the CSV file
    for row in file_reader:
        # Add to the total vote count
        total_votes += 1
        # Get the candidate name from each row
        candidate_name = row[2]
        # If candidate does not match any existing cand's add cand to list
        if candidate_name not in candidate_options:
            # Add candidates name to the candidate list
            candidate_options.append(candidate_name)
            # Track candidates vote count
            candidate_votes[candidate_name] = 0
        # Add vote to that cnadidates count
        candidate_votes[candidate_name] += 1
        # Save the results to a text file
with open(file_to_save, "w") as txt_file:
        # Print final vote count to terminal
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Values: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the txt.file
    txt_file.write(election_results)
    for candidate_name in candidate_votes:
        # Retrieve voute count data
        votes = candidate_votes[candidate_name]
        # Calculate percentages
        vote_percentage = float(votes) / float(total_votes) * 100
        # Print out each candidate's name, vote count, and percentage of votes to the terminal
        candidate_results = (f"{candidate_name}: {vote_percentage:1f}% ({votes:,})\n")
        # Print each candidate, their voter count, % to terminal
        print(candidate_results)
        # Save the candidate results to our text file
        txt_file.write(candidate_results)
        # Determine winning vote count, winning %, and candidate 
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    # Print winning candidates results to terminal
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

    # print(winning_candidate_summary)