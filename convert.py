import pandas as pd

# Read the Excel file
data = pd.read_excel("superstore.xlsx")

# Convert Excel data to CSV
data.to_csv("superstore.xlsx", index=False)

print("Excel file successfully converted to CSV!")