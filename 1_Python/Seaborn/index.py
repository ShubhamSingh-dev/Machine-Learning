# Seaborn: Data visualization library built on top of Matplotlib.
# Seaborn makes it easier to create informative and attractive statistical graphics.

# Importing necessary libraries
import seaborn as sns  # For data visualization
import matplotlib.pyplot as plt  # For rendering plots
import numpy as np  # For numerical operations
import pandas as pd  # For handling datasets

# Note: Seaborn includes some built-in datasets that can be loaded using the `load_dataset()` function.

# Loading the 'tips' dataset (contains data about tips in a restaurant)
tips = sns.load_dataset("tips")
print(tips.head())  # Display the first 5 rows of the dataset

# Setting a theme for the plots
# Seaborn offers different themes to enhance the appearance of plots, such as 'darkgrid', 'whitegrid', 'dark', 'white', and 'ticks'.
sns.set_theme()

# RELATIONAL PLOT
# Relational plots are used to visualize the relationship between two variables.
# Creating a relational plot with the following parameters:
# - data: The dataset to use ('tips')
# - x: The variable for the x-axis ('total_bill')
# - y: The variable for the y-axis ('tip')
# - col: Creates separate plots for each category of 'time' (Lunch/Dinner)
# - hue: Colors the points based on the 'smoker' column
# - style: Shapes the points based on the 'smoker' column
# - size: Adjusts the size of the points based on the 'size' column
sns.relplot(data=tips, x="total_bill", y="tip", col="time", hue="smoker", style="smoker", size="size")
plt.show()  # Render the plot

# Loading the 'iris' dataset (contains data about different iris flower species)
iris = sns.load_dataset("iris")
print(iris.head())  # Display the first 5 rows of the dataset

# SCATTER PLOT
# Scatter plots are used to visualize the relationship between two numerical variables.
# Creating a scatter plot for 'sepal_length' vs 'petal_length' with color differentiation by 'species'.
sns.scatterplot(data=iris, x="sepal_length", y="petal_length", hue="species")
# Creating another scatter plot for 'sepal_length' vs 'petal_width' with color differentiation by 'species'.
sns.scatterplot(data=iris, x="sepal_length", y="petal_width", hue="species")
plt.show()  # Render the plots

# Loading the 'titanic' dataset (contains data about passengers on the Titanic)
titanic = sns.load_dataset("titanic")
print(titanic.head())  # Display the first 5 rows of the dataset

# COUNT PLOT
# Count plots are used to display the count of observations in each category.
# Creating a count plot for the 'class' column, with color differentiation by 'who' (male/female/child).
sns.countplot(data=titanic, x="class", hue="who")
plt.show()  # Render the plot

# Creating another count plot to show the number of passengers who survived (1) or did not survive (0).
sns.countplot(data=titanic, x="survived")
plt.show()  # Render the plot

# BAR PLOT
# Bar plots are used to display an aggregate value (like mean) for each category.
# Creating a bar plot to show the survival rate grouped by 'sex' and differentiated by 'class'.
sns.barplot(x="sex", y="survived", hue="class", data=titanic)
plt.show()  # Render the plot
