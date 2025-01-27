# ----------Exporting a DataFrame to a CSV file---------------

# Importing the pandas library
import pandas as pd

# Creating a Pandas DataFrame
# Importing the California housing dataset from sklearn
from sklearn.datasets import fetch_california_housing

# Loading the dataset
california_dataset = fetch_california_housing(as_frame=True)  # as_frame=True returns a Pandas DataFrame
print(type(california_dataset))

print (california_dataset)

# Creating a Pandas DataFrame
california_df = pd.DataFrame(california_dataset.data,columns=california_dataset.feature_names)

# Exporting the DataFrame to a CSV file
# Do it using
california_df.to_csv('california_housing.csv')

# Runing this code will create a CSV file called california_housing.csv in your folder


# ----------Exporting a DataFrame to a Excel file---------------

#  can be done using
california_df.to_excel('california_housing.xlsx')
