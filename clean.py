import os
import pandas as pd

df = pd.read_csv("combined_data.csv")
otherFile = pd.read_csv("CleanedFile.csv")

for i, row in df.iterrows():
    title = row["Title"]
    citationValue = row["Citation"]
    for k, otherRow in otherFile.iterrows():
        otherTitle = otherRow["Title"]
        if (title.__eq__(otherTitle)):
            print("Match")
            otherFile[k, "Citation"] = citationValue
            df.to_csv(f"cleaned.csv")

df.to_csv("cleaned.csv")
