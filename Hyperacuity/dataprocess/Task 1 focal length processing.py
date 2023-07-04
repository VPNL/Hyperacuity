# import pandas as pd
# import matplotlib.pyplot as plt
# import os
#
# # Read the Excel file into a pandas DataFrame
# file_path = 'Task 1.xlsx'
# data = pd.read_excel(file_path)
#
# # Extract the required columns
# buildings = data['Buildings']
# focal_length = data['focal length']
#
# # Calculate the mean and standard deviation of y-values for each unique x label
# grouped_data = data.groupby('Buildings')['focal length'].agg(['mean', 'std'])
#
# # Extract the mean and standard deviation values
# mean_values = grouped_data['mean']
# std_values = grouped_data['std']
#
# # Set up the plot
# fig, ax = plt.subplots()
#
# # Create the dot plot
# #ax.scatter(buildings, focal_length, color='blue', label='Focal Length')
#
# # Add error bars using mean and standard deviation
# ax.errorbar(mean_values.index, mean_values, yerr=std_values, fmt='o', capsize=4, label='Mean with Std')
#
# # Set x-axis label and rotate the labels if needed
# ax.set_xlabel('Buildings')
# ax.set_xticklabels(mean_values.index, rotation=90)
#
# # Set y-axis label
# ax.set_ylabel('Focal Length (mm)')
#
# plt.tight_layout()
#
#
# output_file = os.path.splitext(file_path)[0] + " Focal Length.png"
# plt.savefig(output_file, bbox_inches='tight')  # Adjust the bounding box to include all elements
# # Display the plot
# plt.show()


import pandas as pd
import matplotlib.pyplot as plt
import os
import statsmodels.api as sm
import statsmodels.formula.api as smf

# Read the Excel file into a pandas DataFrame
file_path = 'Task 1.xlsx'
data = pd.read_excel(file_path)

buildingOrder = ['181 Fremont', '555 California Street', 'Hoover Tower', 'Salesforce', 'Transamerica Pyramid']

# Drop outliers from the data
data = data.groupby('Buildings').apply(lambda x: x[(x['focal length'] >= x['focal length'].quantile(0.25) - 1.5 * (x['focal length'].quantile(0.75) - x['focal length'].quantile(0.25))) &
                                                     (x['focal length'] <= x['focal length'].quantile(0.75) + 1.5 * (x['focal length'].quantile(0.75) - x['focal length'].quantile(0.25)))])

# Drop the specific outlier for '555 California Street'
data = data[(data['Buildings'] != '555 California Street') | (data['focal length'] < 230)] # remove a specific outlier that is not removed by the 1.5 * IQR rule

# Calculate the box plot data for each unique x label
boxplot_data = [data[data['Buildings'] == building]['focal length'] for building in buildingOrder]

# Set up the plot
fig, ax = plt.subplots()

# Create the box plot
ax.boxplot(boxplot_data, labels=data['Buildings'].unique(), vert=True)

# Set x-axis label and rotate the labels if needed
ax.set_xlabel('Buildings')
ax.set_xticklabels(buildingOrder, rotation=90)

# Set y-axis label
ax.set_ylabel('Focal Length (mm)')

plt.tight_layout()

output_file = os.path.splitext(file_path)[0] + " Focal Length boxplot (remove outlier).png"
plt.savefig(output_file, bbox_inches='tight')  # Adjust the bounding box to include all elements

# Perform linear mixed model analysis
lmm_data = data[['focal length', 'Buildings', 'Participants #']]
lmm_data.rename(columns={'Participants #': 'Participants'}, inplace=True)  # Rename the column
lmm_data.rename(columns={'focal length': 'focal_length'}, inplace=True)  # Rename the column
bOrder = pd.Categorical(data['Buildings'], categories=['Hoover Tower', '181 Fremont', '555 California Street', 'Salesforce', 'Transamerica Pyramid'], ordered=True)
lmm_data['Buildings'] = bOrder
lmm_model = smf.mixedlm("focal_length ~ Buildings", lmm_data, groups="Participants")
lmm_results = lmm_model.fit()

print(lmm_results.summary())

# Display the plot
plt.show()



#in this analysis, the focal length for the '181 Fremont' building can be considered as the baseline or reference
#against which the focal lengths of the other buildings ('555 California Street', 'Hoover Tower', 'Salesforce', 'Transamerica Pyramid') are compared.