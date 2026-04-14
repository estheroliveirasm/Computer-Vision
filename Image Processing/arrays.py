import numpy as np

# Creating an array with arange
# np.arange(12) creates elements from 0 to 11
# .reshape(3,4) organizes them into 3 rows and 4 columns
a = np.arange(12).reshape(3,4)

print(a)
print('----------------------')
print(f'Shape: {a.shape}')
print('----------------------')
print(f'Len: {len(a)}')
print('----------------------')

# Changing the shape of an array (reshape)
# The total number of elements (1*2*2*3 = 12) must remain the same
changed = a.reshape(1, 2, 2, 3)

print('Changed: ', changed)
print('----------------------')

# Indexing a multidimensional array
b = np.arange(20).reshape((5,4))
print(b)
print('----------------------')
print('Element at pos 0 and 1:', b[0,1])

# Slicing a multidimensional array
print('----------------------')
c = np.arange(20).reshape(5,4)
print(c)
print('----------------------')
# c[rows, columns] -> rows 0 to 1, columns 0 to 1
print('Slice (first 2 rows and 2 columns):')
print(c[0:2, 0:2])
print('----------------------')

# What is a mask?
# Boolean Masks
a = np.arange(20)
print("Original array:")
print(a)
print("Mask (Condition: a > 5):")
print(a > 5)
print('----------------------')

# Changing data via masks
# All elements where the condition is True will be set to 0
a[a > 5] = 0
print("Array after applying the mask:")
print(a)