import numpy as np

# creating numpy array

# a = np.array([1, 2, 3])
# print(a)
# b = np.array([[1, 2, 3], [4, 5, 6]])
# print(b.shape)
# c = np.zeros((3, 3))
# print(c)
# d = np.eye(3)
# print(d)
# e = np.random.random((3, 3))
# print(e)

# slicing

# f = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# print(f[:, :2])

# Integer Indexing

# a = np.array([[1, 2], [3, 4], [5, 6]])
# print(a[[0, 1, 2], [0, 1, 0]])

# Mask Indexing

# a = np.array([9, 2, 1, 4, 0, 6])
# bool_idx = a > 2
# print(a[bool_idx])

# Array Math

x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])

# Matrix / matrix product;
# both produce a rank 2 array
print(x.dot(y))
print(np.dot(x, y))



