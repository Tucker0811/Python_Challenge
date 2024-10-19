# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
csvpath = os.path.join("Resources", "budget_data.csv")  # Input file path
output_file_path = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
net_total = 0
previous_profit = None
changes = []
greatest_increase = ("", 0)  # (date, amount)
greatest_decrease = ("", 0)  # (date, amount)

# Open and read the csv
with open(csvpath, 'r') as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Process each row of data
    for row in reader:
        date = row[0]
        profit_loss = int(row[1])

        # Track the total months and net total
        total_months += 1
        net_total += profit_loss

        # Calculate changes in profit/losses
        if previous_profit is not None:
            change = profit_loss - previous_profit
            changes.append(change)

            # Calculate the greatest increase in profits (month and amount)
            if change > greatest_increase[1]:
                greatest_increase = (date, change)

            # Calculate the greatest decrease in losses (month and amount)
            if change < greatest_decrease[1]:
                greatest_decrease = (date, change)

        # Update previous profit/loss
        previous_profit = profit_loss

# Calculate the average net change across the months
if changes:
    average_change = sum(changes) / len(changes)
else:
    average_change = 0

# Generate the output summary
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

# Export the results to a text file
with open("financial_analysis.txt", "w") as file:
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${net_total}\n")
    file.write(f"Average Change: ${average_change:.2f}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")
    