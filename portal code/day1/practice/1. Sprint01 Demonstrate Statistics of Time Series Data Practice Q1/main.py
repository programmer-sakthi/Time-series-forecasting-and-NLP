import pandas as pd
import os
import sys

# Read CSV file name
filename = input().strip()

# Construct file path using sys.path[0]
file_path = os.path.join(sys.path[0], filename)

# Check if file exists
if not os.path.isfile(file_path):
    print("File not found.")
    sys.exit()

# Load dataset
df = pd.read_csv(file_path)

# Parse Date column and set as index
df["Date"] = pd.to_datetime(df["Date"])
df.set_index("Date", inplace=True)

# Display first 5 rows
# Display first 5 rows with Date in M/D/YYYY format
print("First 5 rows of the dataset:")

df_display = df.reset_index().head()
df_display["Date"] = df_display["Date"].apply(lambda d: f"{d.month}/{d.day}/{d.year}")

print(df_display)


# Missing values report
print("\nMissing values in dataset:")
print(df.isnull().sum())

# Handle missing values using forward fill
df.fillna(method="ffill", inplace=True)

# Check and remove duplicate rows
duplicate_count = df.duplicated().sum()
df.drop_duplicates(inplace=True)

print("\nNumber of duplicate rows:", duplicate_count)

# Close price summary statistics
print("\nClose price summary statistics:")
print(df["Close"].describe())
