"Cleans the merged files through matching titles with the CleanedFile"

import os
import pandas as pd
import re

def regularMerge():

    original = pd.read_csv("unduplicated.csv")
    otherFile = pd.read_csv("completed2055TWO.csv")

    original["Citation"] = ""

    # Iterating through the original cleaned file
    for i, row in original.iterrows():
        title = row["Title"]
        # Declares found as false for now, until file is found
        found = False

        # Iterating through merged file
        for k, otherRow in otherFile.iterrows():
            otherTitle = otherRow["Title"]

            # If the two titles are the same 
            if (title.__eq__(otherTitle)):
                citationValue = otherRow["Citation"]

                # Information for user to read on console
                print(f"Citation value : {citationValue}")
                print(f"FOUND FILE")
                print(f"Looking for: {title}   Found: {otherTitle}")
                original.at[i, "Citation"] = citationValue
                original.to_csv(f"unduplicated-complete.csv")

                # Set found to true
                found = True
            
            # Stop this iteration of the inner for loop because matching title was found
            if found:
                break;

        # Set citation value to "N/A"
        if not found:
            original.at[i, "Citation"] = "N/A"
        
        # Print out row number
        print(f"Row: {i} COMPLETED \n")

    # Finished iterating through main file!
    print("DONE :)")

    original.to_csv("unduplicated-complete.csv")

def twoFileMerge():
    original = pd.read_csv("completed2055TWO_Unduplicated.csv")
    otherFile = pd.read_csv("combined_data.csv")

    original["Citation"] = ""

    # Iterating through the original cleaned file
    for i, row in original.iterrows():
        title = row["Title"]
        found = False
        originalCitation = row["Original Citation"]
        
        for k, otherRow in otherFile.iterrows():
            otherTitle = otherRow["Title"]
            otherCitationValue = otherRow["Citation"]


            if otherTitle.__eq__(title):
                print(f"Citation value : {otherCitationValue}")
                print(f"FOUND FILE")
                print(f"Looking for: {title}   Found: {otherTitle}")
                original.at[i, "Citation"] = otherCitationValue
                original.to_csv(f"dashesZerosVerified_unduplicated.csv")
            
                found = True
            
            if found:
                break;
            
        if not found:
            original.at[i, "Citation"] = originalCitation

    # Print out row number
        print(f"Row: {i} COMPLETED \n")

    # Finished iterating through main file!
    print("DONE :)")

    original.to_csv("dashesZerosVerified_unduplicated.csv")


# Helper method for remove duplicates to remove all non-alphabet/non-numerical values + strips whitespace
def preprocess_string(input_string):

    if isinstance(input_string, str):
        input_string = re.sub(r"[^a-zA-Z0-9]+", ' ', input_string)
        input_string = input_string.strip()

    return input_string

# Removes duplicates; keeps all but the first value seen
def removeDuplicates():
    data = pd.read_csv("completed2055TWO.csv")
    
    data["Altered Title"] = data["Altered Title"].apply(preprocess_string)
    
    data.sort_values("Altered Title", inplace = True)
    
    # Drop duplicates based on cleaned "Title" column
    data.drop_duplicates(subset = "Altered Title", keep = "first", inplace = True)
    
    data.to_csv("completed2055TWO_Unduplicated.csv", encoding = 'utf-8', index = False)
    
    print("Finished")


def main():
    # regularMerge()
    twoFileMerge()
    # removeDuplicates()

if __name__ == "__main__":
    main()



"""
1) Needs to iterate through the csv of 2055
2) Sees duplicate, removes punctuation/capitilization/etc. BUT saves original
3) Compares, removes duplicate
4) One that remains is the original 
5) Cycle continues and outputs to a csv
"""