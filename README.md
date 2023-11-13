# python-challenge

## Summary
PyBank calculates the following values:

- The total number of months included
- The net total amount of "Profit/Losses" over the period
- The changes in "Profit/Losses" over the period, and then the average
- The greatest increase in profits (date and amount) over the period
- The greatest decrease in profits (date and amount) over the period

The data that is analyzed comes in `csv` format and has two columns: `Date` and `Profit/Losses`.

Example analysis results:
```
Financial Analysis
----------------------------
Total Months: 86
Total: $22564198
Average Change: $-8311.11
Greatest Increase in Profits: Aug-16 ($1862002)
Greatest Decrease in Profits: Feb-14 ($-1825558)
```

## Usage

Go to the directory where the script is located.
`/PyBank`
Run the script from the command line using the following command: 
```
python main.py
```

# PyPoll

## Summary
PyPoll is a set of poll data. 
Composed of three columns: `Voter ID`, `County`, and `Candidate`. 
PyPoll analyzes the votes and calculates each of the following values:

- The total number of votes cast
- A complete list of candidates who received votes
- The percentage of votes each candidate won
- The total number of votes each candidate won
- The winner of the election based on popular vote

Example output results:

```
Election Results
-------------------------
Total Votes: 369711
-------------------------
Charles Casper Stockham: 23.049% (85213)
Diana DeGette: 73.812% (272892)
Raymon Anthony Doane: 3.139% (11606)
-------------------------
Winner: Diana DeGette
-------------------------
```
## Usage

Go to the directory where the script is located.
`/PyPoll`
Run the script from the command line using the following command: 
```
python main.py
```
```
git add .
git commit -m "commit message"
```
5. Push changes to GitHub.
```
git push
```