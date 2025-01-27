# ----------Importing The data from a CSV file to a Pandas DataFrame----------

import pandas as pd 

# CSV file to pandas dataframe
# reading a CSV file
diabetes_df = pd.read_csv('Python/Pandas/diabetes.csv')
print(type(diabetes_df))
print(diabetes_df.head())
print(diabetes_df.shape)

#Loading the data from a excel file to a Pandas DataFrame
# Do it using
# ------pd.read_excel("file path")------