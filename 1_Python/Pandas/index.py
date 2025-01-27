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
# Can be done directly as well like , california_df = california_dataset.frame
print(california_df.head())

# The shape of the DataFrame
print(california_df.shape)

