"""Analyzes CSV spreadsheet for data
- cited articles over the years

"""

import os
import pandas as pd
import math

original = pd.read_csv("unduplicated.csv")

articlePublicationYears = {}

# Iterating through the original cleaned file
for i, row in original.iterrows():
    title = row["Title"]
    year = row["Publication Year"]

    if math.isnan(year):
        year = "N/A"

    if year in articlePublicationYears:
        articlePublicationYears[year] = articlePublicationYears[year] + 1

    else:
        articlePublicationYears[year] = 1

    # print(f"ARTICLE: {i} YEAR: {year}")

total = 0
for key in articlePublicationYears:
    print(f"{key}: {articlePublicationYears[key]}")
    total += articlePublicationYears[key]

print(f"Total: {total}")

    


    
