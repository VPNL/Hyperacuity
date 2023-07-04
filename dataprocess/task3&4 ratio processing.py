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
# names_2 = []
# values_2 = []
#
# for i in range(len(columns_1)):
#     values1List = [t for t in df[columns_1[i]]]
#     names_1.append(columns_1[i])
#     values_1.append(values1List)
#     values2List = [t for t in df[columns_2[i]]]
#     names_2.append(columns_2[i])
#     values_2.append(values2List)
#
# names_3 = []
# values_3 = []
# for i in range(len(values_1)):
#     value3List = []
#     for j in range(len(values_1[i])):
#         if values_1[i][j] != 'Null' and not pd.isna(values_1[i][j]) and values_2[i][j] != 'Null' and not pd.isna(values_2[i][j]):
#             value3List.append(values_1[i][j]/values_2[i][j])
#     values_3.append(value3List)
#     name = 'Task 3 / Task 4 '+ names_1[i].split('3')[1].strip()
#     names_3.append(name)
#
# # Calculate mean and standard deviation for each column C to G
# means_3 = [np.mean(val) for val in values_3]
# stds_3 = [np.std(val) for val in values_3]
#
# # Generate x-coordinates for the dot plot for columns C to G
# x_1 = np.arange(len(names_3))
#
# # Set the figure size
# plt.figure(figsize=(10, 6))
#
# # Create the dot plot for columns C to G with flipped axes and larger dots
# plt.errorbar(x_1, means_3, yerr=stds_3, fmt='o', capsize=5, markersize=8)
#
# # Set the x-ticks to be the names with rotation
# plt.xticks(np.concatenate([x_1]), names_3, rotation=45, ha='right')
#
# # Add labels and title to the plot
# plt.xlabel('Buildings')
# plt.ylabel('Ratio')
# plt.title('Task3&4 Data')
#
#
# for i, mean in enumerate(means_3):
#     plt.text(x_1[i], mean, str(round(mean, 2)), va='bottom')
#
# # Adjust the layout to prevent overlap
# plt.tight_layout()
#
# # Save the figure as a PNG file
# output_file = os.path.splitext(file_path)[0] + " ratio.png"
# plt.savefig(output_file, bbox_inches='tight')  # Adjust the bounding box to include all elements
#
# # Display the plot
# plt.show()


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
# names_3 = []
# values_3 = []
# for i in range(len(values_1)):
#     value3List = []
#     for j in range(len(values_1[i])):
#         if values_1[i][j] != 'Null' and not pd.isna(values_1[i][j]) and values_2[i][j] != 'Null' and not pd.isna(values_2[i][j]):
#             value3List.append(values_1[i][j]/values_2[i][j])
#     values_3.append(value3List)
#     name = 'Task 3 / Task 4 '+ names_1[i].split('3')[1].strip()
#     names_3.append(name)
#
#
# # Calculate mean and standard deviation for each column C to G
# means_1 = [np.mean(val) for val in values_1]
# stds_1 = [np.std(val) for val in values_1]
#
# # Calculate mean and standard deviation for each column H to L
# means_2 = [np.mean(val) for val in values_2]
# stds_2 = [np.std(val) for val in values_2]
#
# # Generate x-coordinates for the box plot for columns C to G
# x_1 = np.arange(len(names_1))
#
# # Generate x-coordinates for the box plot for columns H to L
# x_2 = np.arange(len(names_2)) + 0.5
#
# x_3 = np.arange(len(names_3))
# # Set the figure size
# plt.figure(figsize=(10, 6))
#
# # Create the box plot for columns C to G
# plt.boxplot(values_3, positions=x_3, widths=0.4)
#
# # # Create the box plot for columns H to L
# # plt.boxplot(values_2, positions=x_2, widths=0.4)
#
# # Set the x-ticks to be the names with rotation
# plt.xticks(x_3, names_3, rotation=45, ha='right')
#
# # Add labels and title to the plot
# plt.xlabel('Buildings')
# plt.ylabel('Height (cm)')
# plt.title('Task3&4 Height')
#
# # for i, mean in enumerate(means_1):
# #     plt.text(x_1[i], mean, str(round(mean, 2)), va='bottom')
# # for i, mean in enumerate(means_2):
# #     plt.text(x_2[i], mean, str(round(mean, 2)), va='bottom')
#
# # Adjust the layout to prevent overlap
# plt.tight_layout()
#
# # Save the figure as a PNG file
# output_file = os.path.splitext(file_path)[0] + " height ratio boxplot.png"
# plt.savefig(output_file, bbox_inches='tight')  # Adjust the bounding box to include all elements
#
# # Display the plot
# plt.show()


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
from scipy.stats import ttest_1samp

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
    # Append the column name to the names list for labeling
    names_2.append(col)
    # Append the values list to the values list
    values_2.append(values_list)

names_3 = []
values_3 = []
p_values = []
for i in range(len(values_1)):
    value3List = []
    for j in range(len(values_1[i])):
        if values_1[i][j] != 'Null' and not pd.isna(values_1[i][j]) and values_2[i][j] != 'Null' and not pd.isna(values_2[i][j]):
            value3List.append(values_1[i][j] / values_2[i][j])
    # Drop outliers using 1.5 * IQR threshold
    q1 = np.percentile(value3List, 25)
    q3 = np.percentile(value3List, 75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    value3List = [val for val in value3List if lower_bound <= val <= upper_bound]

    values_3.append(value3List)
    name = 'Task 3 / Task 4 ' + names_1[i].split('3')[1].strip()
    names_3.append(name)
    _, p_value = ttest_1samp(value3List, 1)
    p_values.append(p_value)

# Print the p-values
for i, p_value in enumerate(p_values):
    print(f'{names_3[i]} p-value: {p_value:.3f}')

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

x_3 = np.arange(len(names_3))
# Set the figure size
plt.figure(figsize=(10, 6))

# Create the box plot for columns C to G
plt.boxplot(values_3, positions=x_3, widths=0.4)

# Set the x-ticks to be the names with rotation
plt.xticks(x_3, names_3, rotation=45, ha='right')

# Add asterisks on top of ratios with p-value smaller than 0.05
for i, p_value in enumerate(p_values):
    if p_value < 0.05:
        plt.text(x_3[i], np.max(values_3[i]), '*', ha='center', va='bottom')

# Add labels and title to the plot
plt.xlabel('Buildings')
plt.ylabel('Height Ratio')
plt.title('Task3&4 Height Ratio')

# Adjust the layout to prevent overlap
plt.tight_layout()

# Save the figure as a PNG file
output_file = os.path.splitext(file_path)[0] + " height ratio boxplot (remove outliers).png"
plt.savefig(output_file, bbox_inches='tight')  # Adjust the bounding box to include all elements

# Display the plot
plt.show()


