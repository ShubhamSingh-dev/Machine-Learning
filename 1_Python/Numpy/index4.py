# Mathematical operations in Numpy arrays

import numpy as np

# list
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
print(list1 + list2) # concatenation in case of lists

# Numpy arrays

a = np.random.randint(10,90,(5,5))
b = np.random.randint(10,90,(5,5))

print (a)
print("")
print(b)
print("")

# mathetical operations happens on numpy arrays
print(a + b)
print("")
print(a - b)
print("")
print(a * b)
print("")
print(a / b)
print("")

# another way of mathematical operations

a = np.random.randint(10,90,(3,3))
b = np.random.randint(10,90,(3,3))

print(a)
print("")
print(b)
print("")

print(np.add(a,b))
print("")
print(np.subtract(a,b))
print("")
print(np.multiply(a,b))
print("")
print(np.divide(a,b))
print("")