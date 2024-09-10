import numpy as np

def jacobi_iterative(A, b, X0, TOL=1e-16, N=200):
    """
    Performs Jacobi iterations to solve the system of equations Ax = b,
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
    k = 0

    header = "Iteration\t" + "\t\t".join([f" x{i+1:>12}" for i in range(n)])
    print(header)
    print("--" * len(header))

    while k < N:
        x = np.zeros(n, dtype=np.double)
        for i in range(n):
            sigma = np.dot(A[i, :i], X0[:i]) + np.dot(A[i, i+1:], X0[i+1:])
            x[i] = (b[i] - sigma) / A[i, i]

        print(f"{k+1:<15}" + "\t\t".join([f"{val:<15.6f}" for val in x]))

        if np.max(np.abs(x - X0)) < TOL:
            return x

        X0 = x
        k += 1

    print("Maximum number of iterations exceeded")
    return x

if __name__ == "__main__":
    A = np.array([[3, -1, 1], [0, 1, -1], [1, 1, -2]])
    b = np.array([4, -1, -3])
    x_initial = np.zeros_like(b, dtype=np.double)

    solution = jacobi_iterative(A, b, x_initial)
    print("\nApproximate solution:", solution)
