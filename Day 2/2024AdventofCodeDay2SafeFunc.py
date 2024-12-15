# Pandas is used for reading spreadsheets
import pandas as pd

# Create variable to hold file path for excel file
filePath = 'C:/Users/kayla/Documents/AdventofCode/AdventofCode/Day 2/2024AdventofCode_Day2pt1.xlsx'

# Read the Excel file
df = pd.read_excel(filePath)

# First column contains row names, so this is needed
df.set_index(df.columns[0], inplace=True)

# Display first 5 rows of dataframe
print(df.head())

# Function for Increasing
def increasing(report):
    for level in range(len(report) - 1):
        if report[level] >= report[level + 1]:
            return False
        if (report[level + 1] - report[level]) > 3:
            return False
    return True



# Function for Decreasing (similar to increasing)
def decreasing(report):
    for level in range(len(report) - 1):
        if report[level] <= report[level + 1]:
            return False
        if (report[level] - report[level + 1]) > 3:
            return False
    return True

        
safe = 0
# Read through each report and access each level
for index, row in df.iterrows():
    levelList = [] # Empty array at start of each new report
    print(f"Report: {index}") # Test print that reports are being iterated
    # Read each number in the level (the data of each column within each row)
    for level, value in row.items():
        if pd.notna(value): # Ignore empty cells
            levelList.append(value) # Add values of report for new decicions
            print(f"{level}: {value}") # Test print that only levels that contain data are iterated      
    # Send levelList through functions to test if it passes safe, increment each time a report passes safe.
    if (increasing(levelList)) or (decreasing(levelList)):
        print("Passes safety")
        safe += 1
    print("---") # Seperates each report for better readability

print("Amount of safe reports: ", safe)




    



