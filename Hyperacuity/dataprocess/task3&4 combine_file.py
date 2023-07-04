import os
import pandas as pd

# Specify the folder path containing the directories with CSV files
folder_path = 'D:\Stanford\Hyperacuity\Hyperacuity\Participants'

# Initialize an empty DataFrame to store the combined data
combined_data = pd.DataFrame()

# Iterate over all directories and their files
for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file == 'Task 3&4.csv':  # Check if the file is a CSV
            file_path = os.path.join(root, file)
            df = pd.read_csv(file_path)  # Read the CSV file into a DataFrame
            combined_data = combined_data.append(df, ignore_index=True)  # Append data to the combined DataFrame

# Specify the output Excel file path
output_path = 'D:\Stanford\Hyperacuity\Hyperacuity\Participants\Task 3&4.xlsx'

# Write the combined data to an Excel file
combined_data.to_excel(output_path, index=False)

print('Data successfully combined and saved to', output_path)