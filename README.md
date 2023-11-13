# python-challenge

# Table of Contents
1. [PyBank](#PyBank)
2. [PyPoll](#PyPoll)
3. [Development Getting Started](#Getting-Started)
# PyBank
<img src="./Resources/revenue-per-lead.png" alt="Revenue Per Lead Image">

## Summary
PyBank application is a Python script that analyzes records to calculate each of the following valuesa:

- The total number of months included in the dataset
- The net total amount of "Profit/Losses" over the entire period
- The changes in "Profit/Losses" over the entire period, and then the average of those changes
- The greatest increase in profits (date and amount) over the entire period
- The greatest decrease in profits (date and amount) over the entire period

The data that is analyzed comes in `csv` format and must be composed of two columns: `Date` and `Profit/Losses`.

`Date` is in Jan-10 format and `Profit/Losses` is in integer format.

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


# PyPoll
<img src="./Resources/Vote_counting.png" alt="Polling Station Image">

## Summary
PyPoll is an application that a set of poll data. 
The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. 
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

# Getting Started
