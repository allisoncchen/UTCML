import pandas as pd

df = pd.read_csv("cleaned.csv")
outputFile = "toFind.csv"

# Filter rows with "N/A" citation and save to the output file
df[df["Citation"] == "N/A"].to_csv(outputFile, index=False)

print("Finished")
