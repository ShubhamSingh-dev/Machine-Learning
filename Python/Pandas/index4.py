#  creating a DataFrame with Random values
import pandas as pd
import numpy as np

diabetes_df = pd.read_csv('Python/Pandas/diabetes.csv')
random_df = pd.DataFrame(np.random.rand(20,10)) # DataFrame with 20 rows and 10 columns
print(random_df.head())
# .shape helps in Inspecting the shape of the DataFrame
print(random_df.shape)

# getting first 5 rows of the DataFrame
print(random_df.head())

# getting last 5 rows of the DataFrame
print(random_df.tail())

# Information about the DataFrame
print(random_df.info())

# Find the number of missing values in each column
print(random_df.isnull().sum())

# counting the values based on the labels
print(diabetes_df.value_counts('Outcome')) # Outcome is the column name