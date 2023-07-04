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
# arcminute_in_pixel = data['arcminute degree in each pixel']
#
# # Calculate the mean and standard deviation of y-values for each unique x label
# grouped_data = data.groupby('Buildings')['arcminute degree in each pixel'].agg(['mean', 'std'])
#
# # Extract the mean and standard deviation values
# mean_values = grouped_data['mean']
# std_values = grouped_data['std']
#
# # Set up the plot
# fig, ax = plt.subplots()
#
# # Create the dot plot
# # ax.scatter(buildings, pixel_resolution, color='blue', label='Focal Length')
#
# # Add error bars using mean and standard deviation
# ax.errorbar(mean_values.index, mean_values, yerr=std_values, fmt='o', capsize=4, label='Mean with Std')
#
# # Set x-axis label and rotate the labels if needed
# ax.set_xlabel('Buildings')
# ax.set_xticklabels(mean_values.index, rotation=90)
#
# # Set y-axis label
# ax.set_ylabel('Arcminute Degree in Each Pixel')
#
# plt.tight_layout()
#
#
# output_file = os.path.splitext(file_path)[0] + " arcminute in pixel.png"
# plt.savefig(output_file, bbox_inches='tight')  # Adjust the bounding box to include all elements
# # Display the plot
# plt.show()

# import pandas as pd
# import matplotlib.pyplot as plt
# import os
# import statsmodels.api as sm
# from statsmodels.multivariate.manova import MANOVA
# import statsmodels.formula.api as smf
#
# # Read the Excel file into a pandas DataFrame
# file_path = 'Task 1.xlsx'
# data = pd.read_excel(file_path)
#
# buildingOrder = ['181 Fremont', '555 California Street', 'Hoover Tower', 'Salesforce', 'Transamerica Pyramid']
# # Calculate the box plot data for each unique x label
# boxplot_data = [data[data['Buildings'] == building]['arcminute degree in each pixel'] for building in buildingOrder]
#
# # Set up the plot
# fig, ax = plt.subplots()
#
# # Create the box plot
# ax.boxplot(boxplot_data, labels=data['Buildings'].unique(), vert=True)
#
# # Set x-axis label and rotate the labels if needed
# ax.set_xlabel('Buildings')
# ax.set_xticklabels(buildingOrder, rotation=90)
#
# # Set y-axis label
# ax.set_ylabel('Arcminute Degree in Each Pixel')
#
# plt.tight_layout()
#
# output_file = os.path.splitext(file_path)[0] + " arcminute in pixel boxplot.png"
# plt.savefig(output_file, bbox_inches='tight')  # Adjust the bounding box to include all elements
#
# # Perform one-way repeated MANOVA analysis
# participant_number = data['Participants #']
# manova_data = data[['arcminute degree in each pixel', 'Buildings', 'Participants #']]
# manova_data.rename(columns={'Participants #': 'Participants'}, inplace=True)  # Rename the column
# manova_data.rename(columns={'arcminute degree in each pixel': 'arcminute_degree_in_each_pixel'}, inplace=True)  # Rename the column
# manova = MANOVA.from_formula('C(arcminute_degree_in_each_pixel) ~ C(Buildings)', data=manova_data, groups=data['Participants'])
# # md = smf.mixedlm("C(arcminute_degree_in_each_pixel) ~ C(Buildings)", manova_data, groups=data["Participants #"])
# # mdf = md.fit()
#
# print(manova.mv_test())
# # print(mdf.summary())
#
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

buildingOrder = ['Hoover Tower', '181 Fremont', '555 California Street', 'Salesforce', 'Transamerica Pyramid']
# Calculate the box plot data for each unique x label
boxplot_data = [data[data['Buildings'] == building]['arcminute degree in each pixel'] for building in buildingOrder]

# Set up the plot
fig, ax = plt.subplots()

# Create the box plot
ax.boxplot(boxplot_data, labels=data['Buildings'].unique(), vert=True)

# Set x-axis label and rotate the labels if needed
ax.set_xlabel('Buildings')
ax.set_xticklabels(buildingOrder, rotation=90)

# Set y-axis label
ax.set_ylabel('Arcminute Degree in Each Pixel')

plt.tight_layout()

output_file = os.path.splitext(file_path)[0] + " arcminute in pixel boxplot.png"
plt.savefig(output_file, bbox_inches='tight')  # Adjust the bounding box to include all elements

# Perform linear mixed model analysis
lmm_data = data[['arcminute degree in each pixel', 'Buildings', 'Participants #']]
lmm_data.rename(columns={'Participants #': 'Participants'}, inplace=True)  # Rename the column
lmm_data.rename(columns={'arcminute degree in each pixel': 'arcminute_degree_in_each_pixel'}, inplace=True)  # Rename the column
bOrder = pd.Categorical(data['Buildings'], categories=['Hoover Tower', '181 Fremont', '555 California Street', 'Salesforce', 'Transamerica Pyramid'], ordered=True)
lmm_data['Buildings'] = bOrder
lmm_model = smf.mixedlm("arcminute_degree_in_each_pixel ~ C(Buildings)", lmm_data, groups="Participants")
lmm_results = lmm_model.fit()

print(lmm_results.summary())

# Display the plot
plt.show()

#in this analysis, the arcminute degree in each pixel for the '181 Fremont' building can be considered as the baseline or reference
#against which the focal lengths of the other buildings ('555 California Street', 'Hoover Tower', 'Salesforce', 'Transamerica Pyramid') are compared.