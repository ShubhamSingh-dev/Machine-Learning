# Importing necessary libraries
import seaborn as sns  # For data visualization
import matplotlib.pyplot as plt  # For rendering plots
import numpy as np  # For numerical operations
import pandas as pd  # For handling datasets

# Importing the California housing dataset from scikit-learn
from sklearn.datasets import fetch_california_housing

# Fetching the California housing dataset
# as_frame=True ensures the dataset is returned as a Pandas DataFrame
california_dataset = fetch_california_housing(as_frame=True)
print(type(california_dataset))  # Checking the type of the dataset (it is a Bunch object)

# Creating a Pandas DataFrame from the dataset
# Extracting features (data) and setting the column names
california_df = pd.DataFrame(california_dataset.data, columns=california_dataset.feature_names)

# Alternatively, we could directly use:
# california_df = california_dataset.frame
print(california_df.head())  # Displaying the first 5 rows of the DataFrame

# DISTRIBUTION PLOT
# Distribution plots are used to visualize the distribution of a single variable.

# Plotting the distribution of the 'MedInc' (Median Income) column
# sns.displot() creates a histogram with optional KDE (Kernel Density Estimate)
sns.displot(california_df['MedInc'])

# Using sns.distplot() to create a histogram with a probability curve overlay
# Note: sns.distplot() is deprecated; sns.histplot() or sns.kdeplot() is recommended instead.
sns.distplot(california_df['MedInc'])  # Displays the probability distribution curve
plt.show()  # Render the plots

# CORRELATION
# Correlation measures the relationship between two variables. It can be:
# 1. Positive Correlation: When one variable increases, the other increases.
# 2. Negative Correlation: When one variable increases, the other decreases.

# HEATMAP
# A heatmap is used to visualize the correlation matrix, showing relationships between variables.
# Creating a correlation matrix
correlation = california_df.corr()

# Plotting the heatmap
# figsize: Specifies the size of the plot
# cbar: Adds a color bar to the heatmap
# square: Ensures the cells are square-shaped
# fmt: Sets the format for the annotation text ('.1f' for one decimal point)
# annot: Displays the correlation values inside the heatmap
# annot_kws: Customizes the annotation text size
# cmap: Sets the color palette for the heatmap
plt.figure(figsize=(10, 10))
sns.heatmap(correlation, cbar=True, square=True, fmt='.1f', annot=True, annot_kws={'size': 8}, cmap='Blues')

plt.show()  # Render the heatmap
