import numpy as np

# List
list1 = [1, 2, 3 ,4, 5]
print(list1)
print(type(list1))

# Numpy Array
np_array = np.array([1,2,3,4,5,6,7,8,9,10])
print(np_array)
print(type(np_array))

# Numpy arrays tends to be similar to mathematics matrices

# creating a 1D array
np_array_1D = np.array([1,2,3,4,5,6,7,8,9,10])
print(np_array_1D)

print(np_array_1D.shape) # shape of the array and output is (10,) which means it is 1D array with 10 elements

# creating a 2D array
np_array_2D = np.array([(1,2,3,4), (5,6,7,8)])
print(np_array_2D)

print(np_array_2D.shape) # shape of the array and output is (2,4) which means it is 2D array with 2 rows and 4 columns

# creating a 3D array
np_array_3D = np.array([(1,2,3,4), (5,6,7,8), (9,10,11,12)])
print(np_array_3D)

print(np_array_3D.shape) # shape of the array and output is (3,4) which means it is 3D array with 3 rows and 4 columns

# 2-D array with float values
np_array_2D_float = np.array([(1,2,3,4), (5,6,7,8)], dtype = float)
print(np_array_2D_float)

print(np_array_2D_float.shape)