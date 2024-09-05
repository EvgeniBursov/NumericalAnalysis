import numpy as np
from numpy import power
from math import factorial

# Richardson extrapolation function
def richardson(f, x0, o, h1, v, *control):
    x = np.array(x0)
    d = x.shape[0]
    i = 1
    r = o // 2  # Ensure this is an integer division
    
    while i <= d:
        j = 1
        while j <= r:
            if j == 1:
                h = h1
            else:
                h = h / v
            
            idd = np.eye(d) * h
            xup = x + idd[:, i-1]
            xdown = x - idd[:, i-1]
            fat = f(x, *control)
            fup = f(xup, *control)
            fdown = f(xdown, *control)
            ddu = fup - fat
            ddd = fdown - fat
            
            hp = h
            
            if j == 1:
                dds = np.array([ddu, ddd])
                hhs = np.array([[hp, -hp]])
            else:
                dds = np.concatenate((dds, np.array([ddu, ddd])), axis=0)
                hhs = np.concatenate((hhs, np.array([[hp, -hp]])), axis=1)
            
            j = j + 1
        
        mat = hhs
        
        j = 2
        while j <= o:
            mat = np.concatenate((mat, power(hhs, j) / factorial(j)), axis=0)
            j = j + 1
        
        der = np.dot(np.linalg.inv(np.transpose(mat)), dds)
        
        if i == 1:
            g = der
        else:
            g = np.concatenate((g, der), axis=1)
        
        i = i + 1
    
    return g

# Example 1: Derivative of sin(x) at x = pi/4
def f_sin(x):
    return np.sin(x)

x0 = [np.pi / 4]  # pi/4
derivative_sin = richardson(f_sin, x0, o=4, h1=0.5, v=2)
print("Approximated derivative of sin(x) at pi/4:", derivative_sin)

# Example 2: Derivative of cos(x) at x = 0
def f_cos(x):
    return np.cos(x)

x0 = [0.0]
derivative_cos = richardson(f_cos, x0, o=4, h1=0.5, v=2)
print("Approximated derivative of cos(x) at 0:", derivative_cos)

# Example 3: Derivative of exp(x) at x = 1
def f_exp(x):
    return np.exp(x)

x0 = [1.0]
derivative_exp = richardson(f_exp, x0, o=4, h1=0.5, v=2)
print("Approximated derivative of exp(x) at 1:", derivative_exp)

# Example 4: Derivative of x^2 at x = 2
def f_x2(x):
    return x**2

x0 = [2.0]
derivative_x2 = richardson(f_x2, x0, o=4, h1=0.5, v=2)
print("Approximated derivative of x^2 at 2:", derivative_x2)

# Example 5: Derivative of ln(x) at x = 2
def f_ln(x):
    return np.log(x)

x0 = [2.0]
derivative_ln = richardson(f_ln, x0, o=4, h1=0.5, v=2)
print("Approximated derivative of ln(x) at 2:", derivative_ln)
