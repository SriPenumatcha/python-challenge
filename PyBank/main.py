# import the os module to create file paths across operating systems
import os

# import csv Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

# Initialise variables to store analysis results
total_months = 0
total = 0
previous_profit_loss = 0
total_profit_loss_change = 0
# Initialise greatest_increase list with an empty string '""' and the integer '0'
greatest_increase = ["", 0]
# Initialise greatest_decrease list with an empty string '""' and the integer '0'
greatest_decrease = ["", 0]
profit_loss_changes = []

# Read CSV file using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row first 
    csv_header = next(csvreader)
   
    # Read each row of data after the header
    for row in csvreader:
       # Count the total number of months
        total_months = total_months+1    
        
       # Calculate net total amount of "Profit/Losses"        
        total = total+int(row[1]) 
        
       # Calculate change in profit/loss and append the profit_loss_changes list
        profit_loss_change = int(row[1]) - previous_profit_loss
        if previous_profit_loss != 0:
            profit_loss_changes.append(profit_loss_change)  
            
        # Update previous profit/loss for the next iteration
        previous_profit_loss = int(row[1]) 

        # Find greatest increase in profits 
        if profit_loss_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = profit_loss_change  
            
        # Find greatest decrease in profits 
        if profit_loss_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = profit_loss_change

# Calculate the average of the changes in "Profit/Losses"
average_change = round(sum(profit_loss_changes) / len(profit_loss_changes), 2)

# Print the analysis results
print("\nFinancial Analysis\n")
print("----------------------------------------\n")
print(f"Total Months: {total_months}\n")
print(f"Total: ${total}\n")
print(f"Average Change: ${average_change}\n")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# Write the analysis results to a text file
output_file = os.path.join('analysis', 'financial_analysis.txt')
with open(output_file, 'w') as file:
    file.write("\nFinancial Analysis\n")
    file.write("----------------------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${total}\n")
    file.write(f"Average Change: ${average_change}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")
