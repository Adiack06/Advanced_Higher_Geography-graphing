import pandas as pd

# Read in the CSV file
df = pd.read_csv("islands.csv")

# Group the data by the "island" column
grouped = df.groupby("island ")

# Iterate through each group (island)
for name, group in grouped:
    # Write the group dataframe to a CSV file with the island name as the file name
    group.to_csv(f'{name}.csv', index=False)
