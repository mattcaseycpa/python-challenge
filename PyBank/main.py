import csv
import os

# Path to collect data from the Resources folder
#budget_data_csv = os.path.join('Resources', 'budget_data.csv')
#couldn't get standard join to work
budget_data_csv="/Users/Matt/Desktop/Data Analytics/python-challenge/PyBank/Resources/budget_data.csv"

# Read in the CSV file
with open(budget_data_csv, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    # Create lists to store data
    month = []
    profit_loss = []
    profit_loss_change = []

    # Loop through the data
    for row in csvreader:
        # Add month to list
        month.append(row[0])
        # Add profit/loss to list
        profit_loss.append(int(row[1]))

    # Loop through profit/loss list to calculate change
    for i in range(len(profit_loss)-1):
        this_month_profit_loss=profit_loss[i]
        next_month_profit_loss=profit_loss[i+1]
        # Calculate change and add to list
        profit_loss_change.append(next_month_profit_loss - this_month_profit_loss)

    # Calculate total months
    total_months = len(month)
    # Calculate total profit/loss
    total_profit_loss = sum(profit_loss)
    # Calculate average change
    average_change = sum(profit_loss_change)/len(profit_loss_change)
    # Calculate greatest increase in profits
    greatest_increase_in_profit = max(profit_loss_change)
    # Calculate greatest decrease in profits
    greatest_decrease_in_profit = min(profit_loss_change)

    # Print results
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_profit_loss}")
    print(f"Average Change: ${average_change:.2f}")
    print(f"Greatest Increase in Profits: {month[profit_loss_change.index(greatest_increase_in_profit) + 1]} (${greatest_increase_in_profit})")
    print(f"Greatest Decrease in Profits: {month[profit_loss_change.index(greatest_decrease_in_profit) + 1]} (${greatest_decrease_in_profit})")

# Specify the file to write to
#output_path = os.path.join("analysis", "analysis.txt")
output_path = "/Users/Matt/Desktop/Data Analytics/python-challenge/PyBank/analysis/analysis.txt"

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as analysis_file:

    # Write results to file
    analysis_file.write("Financial Analysis\n")
    analysis_file.write("----------------------------\n")
    analysis_file.write(f"Total Months: {total_months}\n")
    analysis_file.write(f"Total: ${total_profit_loss}\n")
    analysis_file.write(f"Average Change: ${average_change:.2f}\n")
    analysis_file.write(f"Greatest Increase in Profits: {month[profit_loss_change.index(greatest_increase_in_profit) + 1]} (${greatest_increase_in_profit})\n")
    analysis_file.write(f"Greatest Decrease in Profits: {month[profit_loss_change.index(greatest_decrease_in_profit) + 1]} (${greatest_decrease_in_profit})\n")
