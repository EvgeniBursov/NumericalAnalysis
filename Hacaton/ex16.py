import math
from math import e

def TrapezoidalRule(f, n, a, b, tf):
    h = (b - a) / n
    if tf:
        print("Error evaluation En =", round(TrapezError(b, a, h), 6))
    integral = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        integral += f(a + h * i)
    integral *= h
    return integral

def SimpsonRule(f, n, a, b):
    if n % 2 != 0:
        return 0, False
    h = (b - a) / n
    print("Error evaluation En =", round(SimpsonError(b, a, h), 6))
    integral = f(a) + f(b)
    for i in range(1, n):
        k = a + i * h
        if i % 2 == 0:
            integral += 2 * f(k)
        else:
            integral += 4 * f(k)
    integral *= (h / 3)
    return integral, True

def RombergsMethod(f, n, a, b):
    matrix = [[0 for i in range(n)] for j in range(n)]
    for k in range(0, n):
        matrix[k][0] = TrapezoidalRule(f, 2**k, a, b, False)
        for j in range(k):
            matrix[k][j + 1] = (4 ** (j + 1) * matrix[k][j] - matrix[k - 1][j]) / (4 ** (j + 1) - 1)
            print("R[{0}][{1}] = ".format(k, j+1), round(matrix[k][j+1], 6))
    return matrix

def f(x):
    part1 = 2 * x * math.exp(-x) + math.log(2 * x**2)
    part2 = 2 * x**4 + 2 * x**2 - 3 * x - 5
    return part1 * part2
    
def derivative2(x):
    h = 0.0001
    if x + h == x:
        h = abs(x) * 0.0001 + 0.0001
    return (f(x + h) - 2 * f(x) + f(x - h)) / (h * h)

def derivative4(x):
    h = 0.0001
    if x + h == x:
        h = abs(x) * 0.0001 + 0.0001
    return (f(x + 2*h) - 4*f(x + h) + 6*f(x) - 4*f(x - h) + f(x - 2*h)) / (h**4)

def TrapezError(b, a, h):
    xsi = (a + b) / 2
    return -(h**2/12) * (b-a) * derivative2(xsi)

def SimpsonError(b, a, h):
    xsi = (a + b) / 2
    return -(h**4/180) * (b-a) * derivative4(xsi)

def MainFunction():
    n = 4
    method_choice = int(input("What method do you want?\n\t1.Trapez\n\t2. Simpson\n\t3. Rombergd\n"))
    
    if method_choice == 1:
        print("I =", round(TrapezoidalRule(f, n, 0.5, 1, True), 6))
    elif method_choice == 2:
        res = SimpsonRule(f, n, 0.5, 1)
        if res[1]:
            print("I =", round(res[0], 6))
        else:
            print("n must be even!")
    elif method_choice == 3:
        print("I =", round(RombergsMethod(f, n, 0.5, 1)[n-1][n-1], 6))
    else:
        print("Invalid input")

if __name__ == "__main__":
    MainFunction()