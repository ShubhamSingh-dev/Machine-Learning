# Statistical Measures

import pandas as pd
import numpy as np

from sklearn.datasets import fetch_california_housing

california_dataset = fetch_california_housing(as_frame=True)  # as_frame=True returns a Pandas DataFrame
california_df = pd.DataFrame(california_dataset.data,columns=california_dataset.feature_names)


# count or number of values 
print(california_df.count())

# mean or average - column wise
print(california_df.mean())

# standard deviation - column wise
print(california_df.std())

# minimum value 
print(california_df.min())

# maximum value 
print(california_df.max())

# All the statistical measures about the DF
print(california_df.describe())