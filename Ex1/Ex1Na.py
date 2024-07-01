import numpy as np 

"""
GitHub Repo:

Evgeni Bursov
Yael Berko
"""

def calculateNorm(matrix):
    # Get the size of the matrix (number of rows).
    size = len(matrix)

    # Initialize maxNorm to zero. This will hold the maximum row sum.
    maxNorm = 0

    # Iterate through each row of the matrix.
    for i in range(size):
        # Calculate the sum of the absolute values of the elements in the current row.
        rowSum = sum(abs(element) for element in matrix[i])

        # Update maxNorm if the current rowSum is greater than the current maxNorm.
        if rowSum > maxNorm:
            maxNorm = rowSum

    # Return the maximum row sum found, which is the norm of the matrix.
    return maxNorm


def calculateCond(matrix, invMatrix):
    # Calculate the norm of the original matrix using the calculateNorm function.
    normMatrix = calculateNorm(matrix)

    # Calculate the norm of the inverse matrix using the calculateNorm function.
    normInvMatrix = calculateNorm(invMatrix)

    # Return the product of the norms of the original matrix and its inverse.
    return normMatrix * normInvMatrix


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




if __name__ == '__main__':
    matrix = np.array([[1, -1, -2],
                  [2, -3, -5],
                  [-1, 3, 5]])

    try:
        inverMatrix = find_matrix_inverse(matrix)
        print("\nInverse of matrix:\n", inverMatrix)
        print("\n Matrix Norm:\n", calculateNorm(matrix))
        print("\n Inverse Matrix Norm:\n", calculateNorm(inverMatrix))
        print("\n Matrix and Inverse Matrix COND \n", calculateCond(matrix, inverMatrix))
    except ValueError as e:
        print(str(e))




