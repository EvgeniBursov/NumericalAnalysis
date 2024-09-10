import numpy as np
from InverseMatrix import matrix_inverse

def calculate_norm(mat):
    """
    Calculate the maximum row sum norm (infinity norm) of a matrix.
    
    Parameters:
        mat (np.ndarray): The matrix for which the norm is to be calculated.
    
    Returns:
        float: The maximum row sum norm of the matrix.
    """
    return np.max(np.sum(np.abs(mat), axis=1))

def condition_number(A):
    """
    Compute the condition number of matrix A.
    
    Parameters:
        A (np.ndarray): The input square matrix.
    
    Returns:
        float: The condition number of the matrix.
    """
    # Calculate the max norm (infinity norm) of A
    norm_A = calculate_norm(A)

    # Calculate the inverse of A
    A_inv = matrix_inverse(A)

    # Calculate the max norm of the inverse of A
    norm_A_inv = calculate_norm(A_inv)

    # Compute the condition number
    cond = norm_A * norm_A_inv

    # Print the results
    print("Matrix A:")
    print(A)

    print("\nInverse of A:")
    print(A_inv)

    print("\nMax Norm of A:", norm_A)
    print("Max Norm of the Inverse of A:", norm_A_inv)

    return cond

if __name__ == '__main__':
    A = np.array([[2, 1.7, -2.5],
                  [1.24, -2, -0.5],
                  [3, 0.2, 1]])
    cond = condition_number(A)

    print("\nCondition Number:", cond)
