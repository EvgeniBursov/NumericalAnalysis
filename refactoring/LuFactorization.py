import numpy as np
from InverseMatrix import matrix_inverse

def lu_decomposition(A):
    """Compute LU decomposition of matrix."""
    m, n = A.shape
    L = np.eye(m)
    U = A.astype(float)
    
    for j in range(n):
        if U[j, j] == 0:
            if np.any(U[j+1:, j] != 0):
                raise ValueError("LU decomposition does not exist.")
            continue

        for i in range(j + 1, m):
            c = -U[i, j] / U[j, j]
            U[i, j:] += c * U[j, j:]
            L[i, j] = -c

    return L, U

def solving_eq(U, L, b):
    """Solve the system of equations Ax = b using LU decomposition."""
    y = np.linalg.solve(L, b)
    x = np.linalg.solve(U, y)
    return x

if __name__ == '__main__':
    matrix = np.array([[10, 2, 1], [1, 10, 2], [2, 3, 10]])
    vector = np.array([1, 2, 3])

    try:
        # Calculate inverses
        inverMatrix = matrix_inverse(matrix)
        L, U = lu_decomposition(matrix)
        inverMatrixL = matrix_inverse(L)
        inverMatrixU = matrix_inverse(U)

        # Print results
        print("\nInverse of matrix:\n", inverMatrix)
        print("\nLower triangular matrix L:\n", L)
        print("\nUpper triangular matrix U:\n", U)
        print("\nVector b:\n", vector)
        print("\nInverse of matrix L:\n", inverMatrixL)
        print("\nInverse of matrix U:\n", inverMatrixU)
        print("\nResolve: Ax=b the x vector is:\n", solving_eq(U, L, vector))
        
    except ValueError as e:
        print(str(e))
