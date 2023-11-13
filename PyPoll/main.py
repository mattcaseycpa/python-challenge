import csv
import os

# Path to collect data from the Resources folder
#election_data_csv = os.path.join('Resources', 'election_data.csv')
election_data_csv = "/Users/Matt/Desktop/Data Analytics/python-challenge/PyPoll/Resources/election_data.csv"

# Read in the CSV file
with open(election_data_csv, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    # Create lists to store data
    voter_id = []
    county = []
    candidate = []

    # Loop through the data
    for row in csvreader:
        # Add voter id to list
        voter_id.append(row[0])
        # Add county to list
        county.append(row[1])
        # Add candidate to list
        candidate.append(row[2])

    # Calculate total votes
    total_votes = len(voter_id)
    # Calculate unique candidates
    unique_candidates = set(candidate)
    # Calculate votes per candidate
    votes_per_candidate = []
    for i in unique_candidates:
        votes_per_candidate.append(candidate.count(i))
    # Calculate percentage of votes per candidate
    percentage_of_votes_per_candidate = []
    for i in votes_per_candidate:
        percentage_of_votes_per_candidate.append(round(i/total_votes*100, 3))
    # Calculate winner
    winner = list(unique_candidates)[votes_per_candidate.index(max(votes_per_candidate))]

    # Print results
    print("Election Results")
    print("----------------------------")
    print(f"Total Votes: {total_votes}")
    print("----------------------------")
    for i in range(len(unique_candidates)):
        print(f"{list(unique_candidates)[i]}: {percentage_of_votes_per_candidate[i]}% ({votes_per_candidate[i]})")
    print("----------------------------")
    print(f"Winner: {winner}")
    print("----------------------------")

# Specify the file to write to
#output_path = os.path.join("analysis", "analysis.txt")
output_path = "/Users/Matt/Desktop/Data Analytics/python-challenge/PyPoll/analysis/analysis.txt"

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as analysis_file:

    # Write results to file
    analysis_file.write("Election Results\n")
    analysis_file.write("----------------------------\n")
    analysis_file.write(f"Total Votes: {total_votes}\n")
    analysis_file.write("----------------------------\n")
    for i in range(len(unique_candidates)):
        analysis_file.write(f"{list(unique_candidates)[i]}: {percentage_of_votes_per_candidate[i]}% ({votes_per_candidate[i]})\n")
    analysis_file.write("----------------------------\n")
    analysis_file.write(f"Winner: {winner}\n")
    analysis_file.write("----------------------------\n")
