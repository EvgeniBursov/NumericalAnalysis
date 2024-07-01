import numpy as np 

def determinantCalculate(matrix):
    arr = np.array([matrix]) 
    determinant = np.linalg.det(arr)
    return determinant
#jhjij

def calculateNorm(matrix):
    size = len(matrix)
    maxNorm = 0
    for i in range(size):
        if sum(abs(matrix[i])) > maxNorm:
            maxNorm = sum(abs(matrix[i]))
    return maxNorm

def calculateCond(matrix, invMatrix):
    return calculateNorm(matrix)*calculateNorm(invMatrix)


def find_matrix_inverse(matrix):
    """Find the inverse of a non-singular square matrix using elementary row operations."""
    print(f"=================== Finding the inverse of a non-singular matrix using elementary row operations ===================\n{matrix}\n")
    
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
            print("------------------------------------------------------------------------------------------------------------------")
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
                print(f"The matrix after operation {operation_count}:\n{matrix}")
                print("------------------------------------------------------------------------------------------------------------------")
                identity = np.dot(addition_matrix, identity)

    print(f"Total number of operations: {operation_count}")
    return identity




if __name__ == '__main__':
    matrix = np.array([[1, -1, -2],
                  [2, -3, -5],
                  [-1, 3, 5]])

    try:
        inverMatrix = find_matrix_inverse(matrix)
        print("\nInverse of matrix A:\n", inverMatrix)
        #print("=====================================================================================================================")
    except ValueError as e:
        print(str(e))




