import pandas as pd

# Read in the CSV file
df = pd.read_csv("islands.csv")

# Group the data by the "island" column
grouped = df.groupby("island ")

# Specify the column for which to calculate the standard deviation
column = "top "

# Calculate the standard deviation for each group
stddevs = grouped[column].std()

print(stddevs)
