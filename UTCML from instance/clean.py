"Cleans the merged files through matching titles with the CleanedFile"

import os
import pandas as pd

df = pd.read_csv("CleanedFile.csv")
otherFile = pd.read_csv("combined_data.csv")

df["Citation"] = ""

# Iterating through the original cleaned file
for i, row in df.iterrows():
    title = row["Title"]
    found = False
    # Iterating through merged file
    for k, otherRow in otherFile.iterrows():
        otherTitle = otherRow["Title"]

        # If the two titles are the same 
        if (title.__eq__(otherTitle)):
            citationValue = otherRow["Citation"]
            print(f"Citation value : {citationValue}")
            print(f"FOUND FILE")
            print(f"Looking for: {title}   Found: {otherTitle}")
            df.at[i, "Citation"] = citationValue
            df.to_csv(f"cleaned.csv")
            found = True
            break
    if not found:
        df.at[i, "Citation"] = "N/A"
    
    print(f"Row: {i} COMPLETED \n")


print("DONE :)")

df.to_csv("cleaned.csv")
