import numpy as np

"""
Function that finds the inverse of a non-singular matrix
The function performs elementary row operations to transform it into the identity matrix. 
The resulting identity matrix will be the inverse of the input matrix if it is non-singular.
If the input matrix is singular (i.e., its diagonal elements become zero during row operations), it raises an error.
"""

def scale_row(matrix, identity, row_idx, scalar):
    """Scales the specified row of both matrix and identity by the given scalar."""
    matrix[row_idx, :] *= scalar
    identity[row_idx, :] *= scalar
    return matrix, identity

def row_operation(matrix, identity, target_row, source_row, scalar):
    """Performs row addition operation: target_row = target_row + scalar * source_row."""
    matrix[target_row, :] += scalar * matrix[source_row, :]
    identity[target_row, :] += scalar * identity[source_row, :]
    return matrix, identity

def matrix_inverse(matrix):
    """Finds the inverse of a non-singular matrix using elementary row operations."""
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Input matrix must be square.")

    matrix = matrix.astype(float)  # Ensure matrix is float
    n = matrix.shape[0]
    identity = np.identity(n)

    for i in range(n):
        if matrix[i, i] == 0:
            raise ValueError("Matrix is singular, cannot find its inverse.")

        if matrix[i, i] != 1:
            scalar = 1.0 / matrix[i, i]
            matrix, identity = scale_row(matrix, identity, i, scalar)
            print(f"Matrix after scaling row {i+1}:\n {matrix}")
            print("------------------------------------------------------------------------------------------------------------------")

        for j in range(n):
            if i != j:
                scalar = -matrix[j, i]
                matrix, identity = row_operation(matrix, identity, j, i, scalar)
                print(f"Matrix after row operation R{j+1} = R{j+1} + ({scalar}R{i+1}):\n {matrix}")
                print("------------------------------------------------------------------------------------------------------------------")

    return identity


if __name__ == '__main__':
    A = np.array([[1, 2, 3],
                  [2, 3, 4],
                  [3, 4, 6]])

    try:
        A_inverse = matrix_inverse(A)
        print("\nInverse of matrix A:\n", A_inverse)
        print("=====================================================================================================================")

    except ValueError as e:
        print(str(e))
