"Cleans the merged files through matching titles with the CleanedFile"

import os
import pandas as pd


def regularMerge():

    original = pd.read_csv("original2055.csv")
    otherFile = pd.read_csv("combined_data.csv")

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
                original.to_csv(f"complete.csv")

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

    original.to_csv("complete.csv")

def twoFileMerge():
    original = pd.read_csv("completed2055TWO.csv")
    otherFile = pd.read_csv("combined_data.csv")

    original["Citation"] = ""

    # Iterating through the original cleaned file
    for i, row in original.iterrows():
        title = row["Title"]
        found = False
        originalCitation = row["Citation"]
        
        for k, otherRow in otherFile.iterrows():
            otherTitle = otherRow["Title"]
            otherCitationValue = otherRow["Citation"]


            if otherTitle.__eq__(title):
                print(f"Citation value : {otherCitationValue}")
                print(f"FOUND FILE")
                print(f"Looking for: {title}   Found: {otherTitle}")
                original.at[i, "Citation"] = otherCitationValue
                original.to_csv(f"complete.csv")
            
                found = True
            
            if found:
                break;
            
        if not found:
            original.at[i, "Citation"] = originalCitation

    # Print out row number
        print(f"Row: {i} COMPLETED \n")

    # Finished iterating through main file!
    print("DONE :)")

    original.to_csv("complete.csv")



def main():
   # regularMerge()
    twoFileMerge()

if __name__ == "__main__":
    main()