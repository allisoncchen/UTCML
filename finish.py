import pandas as pd

df = pd.read_csv("cleaned.csv")
outputFile = "toFind.csv"

dfs = []

# Create an empty DataFrame to store rows with "N/A" citation
combined_data = pd.DataFrame()

for i, row in df.iterrows():
    
    # For scraping later
    title = row["Title"]
    # Driver of this for loop
    citationValue = row["Citation"]

    nothingFound = "N/A"
    # Couldn't find citation data in combined files
    if nothingFound.__eq__(citationValue):
        # Append the row to the new DataFrame
        # print("here")
        data = pd.DataFrame(row)
        
        dfs.append(row.to_dict())

# Save the filtered DataFrame to the output CSV file

# combined_data = pd.concat(dfs, ignore_index = False)

combined_data = pd.DataFrame(dfs)
combined_data.to_csv(outputFile, encoding='utf-8', index = False)

print("Finished")