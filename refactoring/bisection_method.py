import math
import numpy as np

def max_steps(a, b, err):
    """
    Calculates the minimum number of iterations required to reach the desired accuracy.

    Parameters:
        a (float): Start value.
        b (float): End value.
        err (float): Tolerable error.

    Returns:
        int: The minimum number of iterations required.
    """
    return int(np.floor(- np.log2(err / (b - a)) / np.log2(2) - 1))

def bisection_method(f, a, b, tol=1e-6):
    """
    Performs the bisection method to find the root of a function within an interval [a, b].

    Parameters:
        f (function): Continuous function on the interval [a, b], where f(a) and f(b) have opposite signs.
        a (float): Start value.
        b (float): End value.
        tol (float): Tolerable error. Default is 1e-6.

    Returns:
        float: The approximate root of the function f.
    """
    if np.sign(f(a)) == np.sign(f(b)):
        raise ValueError("The interval [a, b] does not bound a root")

    steps = max_steps(a, b, tol)
    c, k = 0, 0

    print("{:<10} {:<15} {:<15} {:<15} {:<15} {:<15}".format("Iteration", "a", "f(a)", "b", "f(b)", "c", "f(c)"))

    while abs(b - a) > tol and k < steps:
        c = (a + b) / 2

        if f(c) == 0:
            return c

        if f(c) * f(a) < 0:
            b = c
        else:
            a = c

        print("{:<10} {:<15.6f} {:<15.6f} {:<15.6f} {:<15.6f} {:<15.6f}".format(k, a, f(a), b, f(b), c, f(c)))
        k += 1

    return c

if __name__ == '__main__':
    f = lambda x: x**2 - 4 * math.sin(x)
    root = bisection_method(f, 1, 3)
    print(f"\nThe equation f(x) has an approximate root at x = {root}")
