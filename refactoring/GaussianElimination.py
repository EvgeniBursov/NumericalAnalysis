#not done
import numpy as np

def gaussian_elimination(mat):
    N = len(mat)

    singular_flag = forward_substitution(mat)

    if singular_flag != -1:
        if mat[singular_flag][N]:
            return "Singular Matrix (Inconsistent System)"
        else:
            return "Singular Matrix (May have infinitely many solutions)"

    # If matrix is non-singular: get solution to system using backward substitution
    return backward_substitution(mat)


def swap_row(mat, i, j):
    """Swaps two rows in the matrix."""
    mat[i], mat[j] = mat[j], mat[i]


def forward_substitution(mat):
    """Performs forward elimination and partial pivoting."""
    N = len(mat)
    for k in range(N):
        # Partial Pivoting: Find the pivot row with the largest absolute value in the current column
        pivot_row = max(range(k, N), key=lambda i: abs(mat[i][k]))

        # If the pivot element is zero, the matrix is singular
        if abs(mat[pivot_row][k]) < 1e-10:  # Add tolerance to handle floating point issues
            return k  # Matrix is singular

        # Swap the current row with the pivot row
        if pivot_row != k:
            swap_row(mat, k, pivot_row)

        # Perform row reduction
        for i in range(k + 1, N):
            m = mat[i][k] / mat[k][k]
            for j in range(k, N + 1):  # Adjust range to include the augmented column (N+1)
                mat[i][j] -= mat[k][j] * m
            mat[i][k] = 0  # Set the lower triangular matrix elements to zero

    return -1


def backward_substitution(mat):
    """Performs backward substitution to solve the system."""
    N = len(mat)
    x = np.zeros(N)  # An array to store the solution

    # Start calculating from the last equation up to the first
    for i in range(N - 1, -1, -1):
        x[i] = mat[i][N] - sum(mat[i][j] * x[j] for j in range(i + 1, N))
        x[i] /= mat[i][i]

    return x


if __name__ == '__main__':
    # Coefficient matrix with the augmented column (right-hand side values)
    A_b = [
        [-1.41, 2, 0, 4],   # Example system augmented with the right-hand side values
        [1, -1.41, 1, 3],
        [0, 2, -1.41, 2]
    ]

    result = gaussian_elimination(A_b)
    if isinstance(result, str):
        print(result)
    else:
        print("\nSolution for the system:")
        for x in result:
            print("{:.6f}".format(x))
