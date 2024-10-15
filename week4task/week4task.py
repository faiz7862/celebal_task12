import numpy as np
A = np.array([[3, 4, 2],
              [8, 3, 5],
              [6, 6, 7]])
def matrix_multiplication(A):
    return np.dot(A, A)

def matrix_transpose(A):
    return np.transpose(A)

def matrix_determinant(A):
    return np.linalg.det(A)

def eigenvectors(A):
    eigenvalues, eigenvectors = np.linalg.eig(A)
    return eigenvalues, eigenvectors

print("Original Matrix A:\n", A)
print("\nMatrix Multiplication (A * A):\n", matrix_multiplication(A))
print("\nTranspose of Matrix A:\n", matrix_transpose(A))
print("\nDeterminant of Matrix A:\n", matrix_determinant(A))

eigenvalues, eigenvectors = eigenvectors(A)
print("\nEigenvalues of Matrix A:\n", eigenvalues)
print("\nEigenvectors of Matrix A:\n", eigenvectors)
