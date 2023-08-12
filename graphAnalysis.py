"""Analyzes CSV spreadsheet for data
- cited articles over the years

"""

import os
import pandas as pd
import math
import re
import csv

def yearAnalysis():
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

def preprocess_string(input_string):

    if isinstance(input_string, str):
        input_string = re.sub(r"[^a-zA-Z0-9]+", ' ', input_string)
        input_string = input_string.lower()
        input_string = input_string.strip()

    return input_string


def uniquePublications():
    original = pd.read_csv("complete1645.csv")
    outputFile = "publicationCounts.csv"

    articlePublications = {}
    uniquePublications = 0

    # Iterating through the original cleaned file
    for i, row in original.iterrows():
        publication = row["Publication Title"]
        originalPublication = publication 
        publication = preprocess_string(publication)

        if publication in articlePublications:
            articlePublications[publication] = articlePublications[publication] + 1

        else:
            articlePublications[publication] = 1
            uniquePublications = uniquePublications + 1

        # print(f"ARTICLE: {i} YEAR: {year}")

    with open(outputFile, 'w', newline = '') as f:
        writeOut = csv.writer(f)
        writeOut.writerow(["Publication Venue", "Count"])

        total = 0
        for key in articlePublications:
            print(f"{key}: {articlePublications[key]}")
            total += articlePublications[key]
            count = articlePublications[key]

            writeOut.writerow([key, count])

    print(f"Total: {total}")
    print(f"Unique publications: {uniquePublications}")
    print(f'Data written to {outputFile}')


def main():
    # yearAnalysis()
    uniquePublications()

    

if __name__ == "__main__":
    main()


    
