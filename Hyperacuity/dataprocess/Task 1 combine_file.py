import os
import pandas as pd
import re
import haversine as hs
from haversine import Unit

# Specify the folder path containing the directories with CSV files
directory = 'D:\Stanford\Hyperacuity\Hyperacuity\Participants'

dfs = []  # List to store individual DataFrames

for root, dirs, files in os.walk(directory):
    for filename in files:
        if filename.endswith(".csv") and filename != "Task 2_ Comparing Building Heights.csv" and filename != "Task 3&4.csv":
            filepath = os.path.join(root, filename)
            df = pd.read_csv(filepath)
            df_average = df.mean(axis=0, numeric_only=True)
            df_average = pd.DataFrame(df_average).T  # Transpose to create a row DataFrame

            match = re.search(r'result_(.*?)\.csv', filename)
            if match:
                extracted_name = match.group(1)  # Extract the part between "result_" and ".csv"
                formatted_name = extracted_name.replace('_', ' ').title()  # Replace underscores and title case

                df_average.insert(0, 'Buildings', formatted_name)  # Insert filename as the first column

                observe_latitude = df_average['observation point(latitude)'].values[0]
                observe_longitude = df_average['observation point(longitude)'].values[0]
                target_latitude = df_average['target location(latitude)'].values[0]
                target_longitude = df_average['target location(longitude)'].values[0]

                aerial_distance = hs.haversine((observe_latitude, observe_longitude),
                                               (target_latitude, target_longitude), unit=Unit.FEET)

                focalLength = df_average['focal length'].values[0]
                focalDistanceRatio = focalLength / aerial_distance

                df_average['focal length / aerial distance ratio'] = focalDistanceRatio

            dfs.append(df_average)

# Concatenate the list of DataFrames
combined_data = pd.concat(dfs, ignore_index=True)

# Specify the output Excel file path
output_path = 'D:\Stanford\Hyperacuity\Hyperacuity\Participants\Task 1.xlsx'

# Write the combined data to an Excel file
combined_data.to_excel(output_path, index=False)

print('Data successfully combined and saved to', output_path)
