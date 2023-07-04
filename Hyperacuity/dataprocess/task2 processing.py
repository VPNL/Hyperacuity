import pandas as pd
import matplotlib.pyplot as plt
import os

# Read the Excel file
file_path = "Task 2_ Comparing Building Heights (Responses).xlsx"
data = pd.read_excel(file_path)

# Get the values from column C (skipping the first row)
building_heights = data.iloc[1:, 2].values

# Count the occurrences of each building height
building_counts = pd.Series(building_heights).value_counts()

# Set up the figure and axes
fig, ax = plt.subplots(figsize=(8, 6))  # Adjust the figure size as needed

# Plot the pie chart
ax.pie(building_counts, labels=building_counts.index, autopct='%1.1f%%')
ax.set_title("Building Heights Comparison")

# Save the figure as a PNG file
output_file = os.path.splitext(file_path)[0] + ".png"
plt.savefig(output_file, bbox_inches='tight')  # Adjust the bounding box to include all elements

# Display the chart
plt.show()