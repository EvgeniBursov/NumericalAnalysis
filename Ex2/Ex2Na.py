import numpy as np

def find_matrix_inverse(matrix):
    """Find the inverse of a non-singular square matrix using elementary row operations."""
    print(f"Finding the inverse of matrix using elementary row operations \n{matrix}\n")
    
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Input matrix must be square.")

    n = matrix.shape[0]
    identity = np.identity(n)
    operation_count = 0

    # Perform row operations to transform the input matrix into the identity matrix
    for i in range(n):
        if matrix[i, i] == 0:
            raise ValueError("Matrix is singular, cannot find its inverse.")

        if matrix[i, i] != 1:
            # Scale the current row to make the diagonal element 1
            scalar = 1.0 / matrix[i, i]
            scalar_matrix = np.identity(n)
            scalar_matrix[i, i] = scalar
            operation_count += 1
            print(f"Operation {operation_count}: Elementary matrix to make the diagonal element 1:\n{scalar_matrix}\n")
            matrix = np.dot(scalar_matrix, matrix)
            print(f"The matrix after operation {operation_count}:\n{matrix}")
            identity = np.dot(scalar_matrix, identity)

        # Zero out the elements above and below the diagonal
        for j in range(n):
            if i != j:
                scalar = -matrix[j, i]
                addition_matrix = np.identity(n)
                addition_matrix[j, i] = scalar
                operation_count += 1
                print(f"Operation {operation_count}: Elementary matrix for R{j+1} = R{j+1} + ({scalar}R{i+1}):\n{addition_matrix}\n")
                matrix = np.dot(addition_matrix, matrix)
                print(f"The matrix after operation {operation_count}:\n{matrix}\n")
                identity = np.dot(addition_matrix, identity)
    return identity

def lu_decomposition(A):
    """Compute LU decomposition of matrix."""
    m, n = A.shape
    L = np.eye(m)
    U = A.astype(float)  
    
    pivot = 0
    
    for j in range(0, n):
        if U[pivot, j] == 0:
            if np.any(U[pivot + 1:, j]):
                # LU decomposition does not exist if entries below pivot are nonzero
                print("LU decomposition for matrix A does not exist.")
                return np.eye(m), A
            else:
                # All entries below pivot are 0, continue to next column
                continue
        
        # Use nonzero pivot entry to create 0 in each entry below
        for i in range(pivot + 1, m):
            c = -U[i, j] / U[pivot, j]
            U[i, :] = c * U[pivot, :] + U[i, :]
            L[i, pivot] = -c
        pivot += 1
    return L, U

def solving_eq(U,L,b):
    y = np.dot(L,b)
    x = np.dot(U,y)
    return x
    


if __name__ == '__main__':
    matrix = np.array([[1, -1, -2],[2, -3, -5],[-1, 3, 5]])
    vector = np.array([1,2,3])

    try:
        inverMatrix = find_matrix_inverse(matrix)
        L, U = lu_decomposition(matrix)
        inverMatrixL = find_matrix_inverse(L)
        inverMatrixU = find_matrix_inverse(U)
        print("\nInverse of matrix:\n", inverMatrix)
        print("\nLower triangular matrix L:\n", L)
        print("\nUpper triangular matrix U:\n", U)
        print("\nVector b:\n", vector)
        print("\nInverse of matrix L:\n", inverMatrixL)
        print("\nInverse of matrix U:\n", inverMatrixU)
        print("\nResolve: Ax=b the x vector is:\n", solving_eq(inverMatrixU,inverMatrixL,vector))
    except ValueError as e:
        print(str(e))


