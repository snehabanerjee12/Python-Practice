import numpy as np

a = np.zeros((3,4))
print(a)

b = np.arange(0,12,5)
print(b)

b = np.array([[1,2,3],[4,5,6],[7,8,9]])
c = b.flatten()
print(c)

matrix = np.arange(12).reshape(3,4)
flat_view = matrix.ravel() ## changing original matrix
flat_copy = matrix.flatten() ## do not change original matrix
print("Ravel-",flat_view)
print("Flatten-",flat_copy)
