import numpy as np

def gauss_seidel(A, b, X0, TOL=1e-16, N=200):
    """
    Performs Gauss-Seidel iterations to solve the system of equations Ax = b,
    starting from an initial guess, `X0`.

    Parameters:
        A (np.ndarray): NxN matrix for the system.
        b (np.ndarray): Vector of solutions.
        X0 (np.ndarray): Initial guess for the solution. If None, it will be initialized to zero.
        TOL (float): Tolerance for convergence. Default is 1e-16.
        N (int): Maximum number of iterations. Default is 200.

    Returns:
        np.ndarray: The estimated solution.
    """
    n = len(A)
    x = np.zeros(n, dtype=np.double)
    
    header = "Iteration" + "\t\t".join([f"x{i+1:>12}" for i in range(n)])
    separator = "-" * len(header)
    print(header)
    print(separator)

    for k in range(1, N + 1):
        x_old = x.copy()
        
        for i in range(n):
            sigma = np.dot(A[i, :i], x[:i]) + np.dot(A[i, i+1:], X0[i+1:])
            x[i] = (b[i] - sigma) / A[i, i]

        print(f"{k:<15}" + "\t\t".join([f"{val:<15.6f}" for val in x]))

        if np.max(np.abs(x - x_old)) < TOL:
            return x

        X0 = x.copy()

    print("Maximum number of iterations exceeded")
    return x

if __name__ == '__main__':
    A = np.array([[3, -1, 1], [0, 1, -1], [1, 1, -2]])
    b = np.array([4, -1, -3])
    X0 = np.zeros_like(b)

    solution = gauss_seidel(A, b, X0)
    print("\nApproximate solution:", solution)
