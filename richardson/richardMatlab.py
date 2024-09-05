import numpy as np

def richardson_der(f, x0, h_in, N):
    """
    Approximate the 1st and 2nd derivatives of a function f at point x0 using Richardson extrapolation.

    Parameters:
    - f: function to be differentiated
    - x0: point at which the derivatives are approximated
    - h_in: initial step size
    - N: order of the extrapolation

    Returns:
    - f_prime_x0: matrix of Richardson extrapolations for the 1st derivative
    - f_second_x0: matrix of Richardson extrapolations for the 2nd derivative
    """
    # Step values array
    h = np.ones(N)
    h[0] = h_in
    for j in range(1, N):
        h[j] = h[j-1] / 2

    # Preallocate tables for 1st and 2nd derivatives
    f_prime_x0 = np.zeros((N, N+1))
    f_second_x0 = np.zeros((N, N+1))

    # 1st column (step values)
    f_prime_x0[:, 0] = h
    f_second_x0[:, 0] = h

    # 2nd column (central difference formulas for 1st and 2nd derivative)
    for j in range(N):
        f_prime_x0[j, 1] = (f(x0 + h[j]) - f(x0 - h[j])) / (2 * h[j])
        f_second_x0[j, 1] = (f(x0 + h[j]) - 2 * f(x0) + f(x0 - h[j])) / (h[j] ** 2)

    # Other columns (Richardson extrapolates)
    for i in range(2, N+1):
        for j in range(i-1, N):
            f_prime_x0[j, i] = (2**(2*(i-1)) * f_prime_x0[j, i-1] - f_prime_x0[j-1, i-1]) / (2**(2*(i-1)) - 1)
            f_second_x0[j, i] = (2**(2*(i-1)) * f_second_x0[j, i-1] - f_second_x0[j-1, i-1]) / (2**(2*(i-1)) - 1)

    return f_prime_x0, f_second_x0

# Define the example functions
def example_function_sin(x):
    return np.sin(x)

def example_function_cos(x):
    return np.cos(x)

def example_function_exp(x):
    return np.exp(x)

def example_function_x2(x):
    return x**2

# Parameters
h_in = 0.1
N = 4

# Compute derivatives for sin(x) at x0 = pi/4
x0_sin = np.pi / 4
f_prime_x0_sin, f_second_x0_sin = richardson_der(example_function_sin, x0_sin, h_in, N)
print("Approximated derivative of sin(x) at pi/4:")
print("First Derivative:\n", f_prime_x0_sin)
print("Second Derivative:\n", f_second_x0_sin)

# Compute derivatives for cos(x) at x0 = 0
x0_cos = 0
f_prime_x0_cos, f_second_x0_cos = richardson_der(example_function_cos, x0_cos, h_in, N)
print("Approximated derivative of cos(x) at 0:")
print("First Derivative:\n", f_prime_x0_cos)
print("Second Derivative:\n", f_second_x0_cos)

# Compute derivatives for exp(x) at x0 = 1
x0_exp = 1
f_prime_x0_exp, f_second_x0_exp = richardson_der(example_function_exp, x0_exp, h_in, N)
print("Approximated derivative of exp(x) at 1:")
print("First Derivative:\n", f_prime_x0_exp)
print("Second Derivative:\n", f_second_x0_exp)

# Compute derivatives for x^2 at x0 = 2
x0_x2 = 2
f_prime_x0_x2, f_second_x0_x2 = richardson_der(example_function_x2, x0_x2, h_in, N)
print("Approximated derivative of x^2 at 2:")
print("First Derivative:\n", f_prime_x0_x2)
print("Second Derivative:\n", f_second_x0_x2)
