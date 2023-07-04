import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt
import os
from scipy import stats


ARM_LENGTH = 70 # based on google search, the arm length distance of a typical human holding object like ipad is around 70cm

file_path = 'Task 3&4.xlsx'

# Read the Excel file, df is the estimation, df2 is the ground truth
df = pd.read_excel('Task 3&4.xlsx')

columns_to_extract = [1] + list(range(7, 12))  # 2nd column and columns 8-12
df = df.iloc[:, columns_to_extract]

columns = df.columns[1:]

# Iterate over the columns
for column in columns:
    df[column] = df[column].apply(lambda x: math.degrees(math.atan(x / ARM_LENGTH)) * 60 if x != 'Null' else x)

df = pd.melt(df, id_vars='ID', var_name='Building', value_name='Length')

df['Building'] = df['Building'].str.replace('Task 4 ', '').str.replace(' \(cm\)', '')
df['Building'] = df['Building'].replace('555 California', '555 California Street')
df['Building'] = df['Building'].replace('Hoover', 'Hoover Tower')
df['Building'] = df['Building'].replace('Transamerica', 'Transamerica Pyramid')

df = df[['Building', 'ID', 'Length']]
df = df.rename(columns={'Building': 'Buildings', 'ID': 'Participants #', 'Length':'target location(relative height(arcminute)'})

df2 = pd.read_excel('Task 1.xlsx')
df2 = df2.iloc[:, [0, 1, 24]]

merged_df = pd.merge(df, df2, on=['Buildings', 'Participants #'])


t_statistic, p_value = stats.ttest_rel(merged_df.iloc[:, 2], merged_df.iloc[:, 3])
print("T-Test between estimation and ground truth across all buildings")
print("T-statistic:", t_statistic)
print("P-value:", p_value)
print()


names_1 = []
values_1 = []
names_2 = []
values_2 = []

grouped = merged_df.groupby('Buildings')
for name, group in grouped:
    t_statistic, p_value = stats.ttest_rel(group.iloc[:, 2], group.iloc[:, 3])
    print("T-Test between estimation and ground truth for", name)
    print("T-statistic:", t_statistic)
    print("p-value:", p_value)
    print()

    name1 = name + ' estimation'
    names_1.append(name1)

    name2 = name + ' ground truth'
    names_2.append(name2)

    values_1.append(group.iloc[:, 2])
    values_2.append(group.iloc[:, 3])

merged_df.to_excel('Task 4 & Ground truth.xlsx')

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
plt.title('Task4 & ground truth Height (arcminute)')

# Calculate mean and standard deviation for each column C to G
means_1 = [np.mean(val) for val in values_1]
stds_1 = [np.std(val) for val in values_1]

# Calculate mean and standard deviation for each column H to L
means_2 = [np.mean(val) for val in values_2]
stds_2 = [np.std(val) for val in values_2]

for i, mean in enumerate(means_1):
    plt.text(x_1[i], mean, str(round(mean, 2)), va='bottom')
for i, mean in enumerate(means_2):
    plt.text(x_2[i], mean, str(round(mean, 2)), va='bottom')

# Adjust the layout to prevent overlap
plt.tight_layout()

# Save the figure as a PNG file
output_file = os.path.splitext(file_path)[0] + " hypo testing boxplot (arcminute).png"
plt.savefig(output_file, bbox_inches='tight')  # Adjust the bounding box to include all elements

# Display the plot
plt.show()