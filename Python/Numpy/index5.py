# Array Manupulation

import numpy as np

a = np.random.randint(0,10,(2,3))
print(a)
print(a.shape) # output is (2,3)
print("")

# transpose
trans = np.transpose(a)
print(trans)
print(trans.shape) # output is (3,2) got transposed
print("")
#or 
trans2 = a.T
print(trans2)
print(trans2.shape)

# reshape
reshape = a.reshape(3,2)
print(reshape)
print(reshape.shape)