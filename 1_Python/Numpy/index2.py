import numpy as np

# Intital place holders in Numpy arrays

# Creating a numpy array of zeros
x = np.zeros((5,5)) # This is a 5x5 matrix of zeros
print(x)
print(" ")


# Creating a numpy array of ones
x = np.ones((3,5)) # This is a 3x5 matrix of ones
print(x)
print(" ")

# Creating a numpy array of particular numbers
x = np.full((5,4), 5) # This is a 5x4 matrix of 5s
print(x)
print(" ")

# creatinf a identity matrix
x = np.eye(4) # This is a 4x4 identity matrix
print(x)
print(" ")

# creating a numpy array of random numbers

x = np.random.random((3,4)) # This is a 3x4 matrix of random numbers
print(x)
print(" ")

# creating a numpy array of random integers within a range

x = np.random.randint(10,100, (3,4)) # This is a 3x4 matrix of random integers within a range of 10 to 100
print(x)
print(" ")

# array of evenly spaced numbers

x = np.linspace(0,50,5) # This is a 1D array of 5 numbers evenly spaced between 0 and 10
print(x)
print(" ")

# array of evenly spaced numbers specifying the steps

x = np.arange(0,50,5) # This is a 1D array of 5 numbers evenly spaced between 0 and 10
print(x)
print(" ")

# convert a list to a numpy array

list2 = [10,20,30,40,50]
x = np.asarray(list2)
print(x)
print(type(x))
print(" ")

