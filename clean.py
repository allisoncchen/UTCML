"Cleans the merged files through matching titles with the CleanedFile"

import os
import pandas as pd
import re
import math 

def regularMerge():

    original = pd.read_csv("addNumbers.csv", encoding = 'utf-8')
    otherFile = pd.read_csv("correctFormat.csv", encoding = 'utf-8')

    otherFile["Citation"] = ""

    # Iterating through the unduplicated file with citations
    for i, row in original.iterrows():
        rowNumber = row["Unnamed: 0"] # row with number
        found = False

        for k, otherRow in otherFile.iterrows():
            otherRowNumber = otherRow["Row"]

            # If the two titles are the same 
            if ((rowNumber) == (otherRowNumber)):
                citation = row["Citation"] # grabbing citation value

                print(f"Looking for row: {i}   Found: {k}")
                otherFile.at[k, "Citation"] = citation
                otherFile.to_csv(f"addCitations.csv", encoding = 'utf-8')

                # Set found to true
                found = True
            
            # Stop this iteration of the inner for loop because matching title was found
            if found:
                break;

        # Set citation value to "N/A"
        if not found:
            otherFile.at[k, "Citation"] = ""
            otherFile.to_csv(f"addCitations.csv", encoding = 'utf-8')
        
        # Print out row number
        print(f"Row: {i} COMPLETED \n")

    # Finished iterating through main file!
    print("DONE :)")

    otherFile.to_csv("addCitations.csv", encoding = 'utf-8')

def twoFileMerge():
    original = pd.read_csv("completed_unduplicated.csv")
    otherFile = pd.read_csv("combinedReruns_unduplicate.csv")

    # Initialize the "Citation" column in the original DataFrame
    original["Citation"] = ""

    # Iterating through the original cleaned file
    for i, row in original.iterrows():
        title = row["Title"]
        print(f"Title: {title}")
        found = False
        originalCitation = row["Original Citation"]
        print(f"\nOriginal Citation {originalCitation}")

        for k, otherRow in otherFile.iterrows():
            otherTitle = otherRow["Title"]
            otherCitationValue = otherRow["Citation"]

            # Handling NaN comparison correctly
            if pd.notna(otherTitle):
                if title == otherTitle:
                    print(f"Citation value: {otherCitationValue}")
                    print("FOUND FILE")
                    print(f"Looking for: {title}   Found: {otherTitle}")
                    original.at[i, "Citation"] = otherCitationValue
                    original.to_csv("completed-combinedReruns_unduplicate.csv")
                    found = True
                    break

        if not found:
            original.at[i, "Citation"] = originalCitation

    # Save the final DataFrame to a new CSV file
    original.to_csv("completed-combinedReruns_unduplicate.csv", index=False)

    # Finish message
    print("Merge completed successfully.") 
    

    original.to_csv("completed-combinedReruns_unduplicate.csv")


# Helper method for remove duplicates to remove all non-alphabet/non-numerical values + strips whitespace
def preprocess_string(input_string):

    if isinstance(input_string, str):
        input_string = re.sub(r"[^a-zA-Z0-9]+", ' ', input_string)
        input_string = input_string.strip()

    return input_string

# Removes duplicates; keeps all but the first value seen
def removeDuplicates():
    data = pd.read_csv("dashesZerosVerified_unduplicated.csv")
    
    data["Altered Abstract"] = data["Altered Abstract"].apply(preprocess_string)
    
    data.sort_values("Altered Abstract", inplace = True)
    
    # Drop duplicates based on cleaned "Abstract" column
    data.drop_duplicates(subset = "Altered Abstract", keep = "first", inplace = True)
    
    data.to_csv("completed_unduplicated.csv", encoding = 'utf-8', index = False)
    
    print("Finished")


def main():
    regularMerge()
    # twoFileMerge()
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