# Manipulating a DataFrame

import pandas as pd
import numpy as np

from sklearn.datasets import fetch_california_housing

california_dataset = fetch_california_housing(as_frame=True)  # as_frame=True returns a Pandas DataFrame
california_df = pd.DataFrame(california_dataset.data,columns=california_dataset.feature_names)

# Adding a new column
california_df['price_per_room'] = california_df['MedInc'] / california_df['HouseAge']
print(california_df.head())

# Removing a column
del california_df['price_per_room']
# or
california_df = california_df.drop(columns='price_per_room',axis=1) 
print(california_df.head())

# Removing a row
california_df = california_df.drop(0)
# or
california_df = california_df.drop(index=0 , axis=0)
print(california_df.head())

# Locating a Row using index value 
california_df.iloc[2]

# Locating a column using index value
california_df.iloc[:,0] # first column 
california_df.iloc[:,1] # 2 column 
california_df.iloc[:,2] # 3 column 
california_df.iloc[:,-1] # last column 


# Correlation :

california_df.corr() #+ve sign means positive correlation and -ve sign means negative correlation