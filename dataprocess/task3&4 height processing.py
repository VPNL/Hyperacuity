# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
# import os
#
# # Read the Excel file
# file_path = "Task 3&4.xlsx"
# df = pd.read_excel(file_path)
#
# # Select columns C to G
# columns_1 = df.columns[2:7]
# # Select columns H to L
# columns_2 = df.columns[7:12]
#
# # Create empty lists to store data for columns C to G
# names_1 = []
# values_1 = []
#
# # Iterate over the selected columns C to G
# for col in columns_1:
#     # Drop null values and convert to a list
#     values_list = [t for t in df[col] if t != 'Null' and not pd.isna(t)]
#     # Append the column name to the names list for labeling
#     names_1.append(col)
#     # Append the values list to the values list
#     values_1.append(values_list)
#
# # Create empty lists to store data for columns H to L
# names_2 = []
# values_2 = []
#
# # Iterate over the selected columns H to L
# for col in columns_2:
#     # Drop null values and convert to a list
#     values_list = [t for t in df[col] if t != 'Null' and not pd.isna(t)]
#     # Append the column name to the names list for labeling
#     names_2.append(col)
#     # Append the values list to the values list
#     values_2.append(values_list)
#
# # Calculate mean and standard deviation for each column C to G
# means_1 = [np.mean(val) for val in values_1]
# stds_1 = [np.std(val) for val in values_1]
#
# # Calculate mean and standard deviation for each column H to L
# means_2 = [np.mean(val) for val in values_2]
# stds_2 = [np.std(val) for val in values_2]
#
# # Generate x-coordinates for the dot plot for columns C to G
# x_1 = np.arange(len(names_1))
#
# # Generate x-coordinates for the dot plot for columns H to L
# x_2 = np.arange(len(names_2)) + 0.5
#
# # Set the figure size
# plt.figure(figsize=(10, 6))
#
# # Create the dot plot for columns C to G with flipped axes and larger dots
# plt.errorbar(x_1, means_1, yerr=stds_1, fmt='o', capsize=5, markersize=8)
#
# # Create the dot plot for columns H to L with flipped axes and larger dots
# plt.errorbar(x_2, means_2, yerr=stds_2, fmt='o', capsize=5, markersize=8)
#
# # Set the x-ticks to be the names with rotation
# plt.xticks(np.concatenate([x_1, x_2]), names_1 + names_2, rotation=45, ha='right')
#
# # Add labels and title to the plot
# plt.xlabel('Buildings')
# plt.ylabel('Height (cm)')
# plt.title('Task3&4 Height')
#
#
# for i, mean in enumerate(means_1):
#     plt.text(x_1[i], mean, str(round(mean, 2)), va='bottom')
# for i, mean in enumerate(means_2):
#     plt.text(x_2[i], mean, str(round(mean, 2)), va='bottom')
#
# # Adjust the layout to prevent overlap
# plt.tight_layout()
#
# # Save the figure as a PNG file
# output_file = os.path.splitext(file_path)[0] + " height.png"
# plt.savefig(output_file, bbox_inches='tight')  # Adjust the bounding box to include all elements
#
# # Display the plot
# plt.show()


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import math

ARM_LENGTH = 70 # based on google search, the arm length distance of a typical human holding object like ipad is around 70cm


# Read the Excel file
file_path = "Task 3&4.xlsx"
df = pd.read_excel(file_path)

# Select columns C to G
columns_1 = df.columns[2:7]
# Select columns H to L
columns_2 = df.columns[7:12]

# Create empty lists to store data for columns C to G
names_1 = []
values_1 = []

# Iterate over the selected columns C to G
for col in columns_1:
    # Drop null values and convert to a list
    values_list = [t for t in df[col] if t != 'Null' and not pd.isna(t)]

    # turn to visual angle
    for i in range(len(values_list)):
        values_list[i] = math.degrees(math.atan(values_list[i] / ARM_LENGTH)) * 60

    # Append the column name to the names list for labeling
    names_1.append(col)
    # Append the values list to the values list
    values_1.append(values_list)

# Create empty lists to store data for columns H to L
names_2 = []
values_2 = []

# Iterate over the selected columns H to L
for col in columns_2:
    # Drop null values and convert to a list
    values_list = [t for t in df[col] if t != 'Null' and not pd.isna(t)]

    # turn to visual angle
    for i in range(len(values_list)):
        values_list[i] = math.degrees(math.atan(values_list[i] / ARM_LENGTH)) * 60

    # Append the column name to the names list for labeling
    names_2.append(col)
    # Append the values list to the values list
    values_2.append(values_list)

# Calculate mean and standard deviation for each column C to G
means_1 = [np.mean(val) for val in values_1]
stds_1 = [np.std(val) for val in values_1]

# Calculate mean and standard deviation for each column H to L
means_2 = [np.mean(val) for val in values_2]
stds_2 = [np.std(val) for val in values_2]

# Generate x-coordinates for the box plot for columns C to G
x_1 = np.arange(len(names_1))

# Generate x-coordinates for the box plot for columns H to L
x_2 = np.arange(len(names_2)) + 0.5

# Set the figure size
plt.figure(figsize=(10, 6))

# Create the box plot for columns C to G
plt.boxplot(values_1, positions=x_1, widths=0.4)

# Create the box plot for columns H to L
plt.boxplot(values_2, positions=x_2, widths=0.4)

# Set the x-ticks to be the names with rotation
plt.xticks(np.concatenate([x_1, x_2]), names_1 + names_2, rotation=45, ha='right')

# Add labels and title to the plot
plt.xlabel('Buildings')
plt.ylabel('Height (arcminute)')
plt.title('Task3&4 Height')

for i, mean in enumerate(means_1):
    plt.text(x_1[i], mean, str(round(mean, 2)), va='bottom')
for i, mean in enumerate(means_2):
    plt.text(x_2[i], mean, str(round(mean, 2)), va='bottom')

# Adjust the layout to prevent overlap
plt.tight_layout()

# Save the figure as a PNG file
output_file = os.path.splitext(file_path)[0] + " height boxplot (arcminute).png"
plt.savefig(output_file, bbox_inches='tight')  # Adjust the bounding box to include all elements

# Display the plot
plt.show()

