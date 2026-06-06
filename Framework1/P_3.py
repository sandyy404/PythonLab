# Perform matrix operations using NumPy including transpose, determinant, and inverse.

import numpy as np

matrix = np.array([[1, 2],
                   [3, 4]])

print("Matrix:")
print(matrix)

print("\nTranspose:")
print(matrix.T)

print("\nDeterminant:")
print(np.linalg.det(matrix))

print("\nInverse:")
print(np.linalg.inv(matrix))

