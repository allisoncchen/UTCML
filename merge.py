"Merges all of the CSV files together collected from the citation script"

import os
import pandas as pd


def get_numeric_value(file_name):
    return int(file_name[0 : 4])

folder_path = 'dashes'  # Replace with the actual folder path

# Get a list of all CSV files in the folder
csv_files = sorted([file for file in os.listdir(folder_path) if file.endswith('.csv')])

# Sort the CSV's by title (honestly, not necessary with clean.py)
csv_files = sorted(csv_files, key = get_numeric_value)

# Create an empty DataFrame to store the combined data
combined_data = pd.DataFrame()

dfs= []

for file in csv_files: # For every csv file in the folder
    
    # Just for user purposes
    print(f"File name: {file}")

    filePath = os.path.join(folder_path, file) # Getting the file path to each individual 
    

    df = pd.read_csv(filePath) # Information from csv file

    # print(f"File Data: {fileInfo}")

    # Append the data to the combined 
    dfs.append(df)

# Concat list of data frames to one data frame
combined_data = pd.concat(dfs, ignore_index = False)

# Save the combined data to a CSV file
combined_file_name = 'combined60.csv'
combined_data.to_csv(combined_file_name, encoding='utf-8', index=False)

# Finish message
print(f"Combined data saved to '{combined_file_name}'.")


