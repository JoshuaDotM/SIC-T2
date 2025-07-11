import numpy as np

array1 = np.zeros(3)
array2 = np.zeros((1, 4))
array3 = np.zeros((2, 5))

print(array1[0], array1[2])
print(array2[0][0], array2[0][3])
print(array3[1][0], array3[1][3])

arr = np.arange(1, 10)
print(arr, '\n')

# Reshape to 3x3 matrix
arr = arr.reshape(3, 3)
print(arr, '\n')

# Reshape back to the original size
arr = arr.reshape(9)
print(arr)

arr = arr.reshape(2, 5) # ValueError
print(arr)