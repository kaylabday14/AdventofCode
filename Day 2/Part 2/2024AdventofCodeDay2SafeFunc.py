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

def dampener(report):
    i = 0
    for i in range(len(report)):
        # Create a copy of the report to avoid modifying the original list during iteration
        tempReport = report[:]
        # Remove the element at index i (Removing a level from a report)
        tempReport.pop(i)
        
        # Check if the remaining levels are either increasing or decreasing
        if increasing(tempReport) or decreasing(tempReport):
            return True
    # Return at end of loop otherwise the loop will end early  
    return False


        
        
        
safe = 0
dampenerSafe = 0
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
    # If levelList doesn't pass the first safety check, then send it through the dampener function
    elif (dampener(levelList)):
        dampenerSafe +=1

    print("---") # Seperates each report for better readability

total = safe + dampenerSafe
print("Amount of safe reports: ", safe)
print("Amount of reports safe with dampener: ", dampenerSafe)
print("Total of safe reports: ", total)



    



