"Compiles all of the articles that don't have a citation value into a CSV"
import pandas as pd

def collectNotAvailable():

    df = pd.read_csv("cleaned.csv")
    outputFile = "toRerun.csv"

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
            # data = pd.DataFrame(row)
            
            dfs.append(row.to_dict())

    combined_data = pd.DataFrame(dfs)
    combined_data.to_csv(outputFile, encoding='utf-8', index = False)

    print("Finished")


def collectOneZero():
    df = pd.read_csv("dashesZerosVerified_unduplicated.csv")
    outputFile = "toRerun.csv"

    dfs = []

    # Create an empty DataFrame to store rows with "N/A" citation
    combined_data = pd.DataFrame()

    for i, row in df.iterrows():
    
        # For scraping later
        title = row["Title"]
        # Driver of this for loop
        citationValue = row["Citation"]

        nothingFound = "-"
        zero = "0"

        # Couldn't find citation data in combined files
        if nothingFound.__eq__(citationValue) or zero.__eq__(citationValue):
            print(f"{i} {zero == citationValue}")
            # Append the row to the new DataFrame
            # print("here")
            # data = pd.DataFrame(row)
            
            dfs.append(row.to_dict())

    combined_data = pd.DataFrame(dfs)
    combined_data.to_csv(outputFile, encoding='utf-8', index = False)

    print("Finished")



def main():
   #  collectNotAvailable()
   collectOneZero()


if __name__ == "__main__":
    main()