import matplotlib.pyplot as plt
import numpy as np

# Example data: names, values, and errors
names = ['A', 'B', 'C', 'D', 'E']
values = [np.random.normal(5, 1, 100), np.random.normal(7, 0.5, 100),
          np.random.normal(4, 1.5, 100), np.random.normal(6, 0.8, 100),
          np.random.normal(5.5, 1.2, 100)]

# Calculate mean and standard deviation for each name
means = [np.mean(val) for val in values]
stds = [np.std(val) for val in values]

# Generate x-coordinates for the dot plot
x = np.arange(len(names))

# Create the dot plot with flipped axes
plt.errorbar(x, means, yerr=stds, fmt='o', capsize=5)

# Set the x-ticks to be the names
plt.xticks(x, names)

# Add labels and title to the plot
plt.xlabel('Names')
plt.ylabel('Values')
plt.title('Dot Plot with Error Bars')

# Display the plot
plt.show()