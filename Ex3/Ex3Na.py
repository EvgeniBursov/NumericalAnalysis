"""
GitHub Repo:


Evgeni Bursov
Yael Berko
"""

import numpy as np

def CheckDominantDiagonal(matrix):
    """
    Function for testing a dominant diagonal
    :param matrix: Matrix nxn
    :return: True or false if there is a dominant diagonal
    """
    for i in range(len(matrix)):
        sum = 0
        for j in range(len(matrix)):
            if i != j:
                sum += abs(matrix[i][j])
        if abs(matrix[i][i]) < sum:
            return False
    return True

def matrixDLUdissasembly(matrix):
    """
    :param matrix: matrix nXn
    :return: Breaking down matrices L U D
    """
    D, L, U = [], [], []
    for x, row in enumerate(matrix):
        D.append([]), L.append([]), U.append([])
        for y, value in enumerate(row):
            if x == y:
                D[x].append(value), L[x].append(0), U[x].append(0)
            elif x < y:
                D[x].append(0), L[x].append(0), U[x].append(value)
            elif x > y:
                D[x].append(0), L[x].append(value), U[x].append(0)
    return np.array(D), np.array(L), np.array(U)

def JacobiMethod(matrix, vector, epsilon, previous, counter):
    """
    Function for solving a set of equations according to the Jacobi method
    :param matrix: Matrix nxn
    :param vector: Vector n
    :param epsilon: Stop Conditions
    :param previous: Result vector
    :param counter: Number of iterations
    """
    next_guess = np.zeros_like(previous)
    for i in range(len(matrix)):
        ins = 0
        for j in range(len(matrix)):
            if i != j:
                ins += matrix[i][j] * previous[j]
        next_guess[i] = 1 / matrix[i][i] * (vector[i] - ins)

    print(f"Iteration no. {counter} {next_guess.tolist()}")

    if np.linalg.norm(next_guess - previous, ord=np.inf) < epsilon:
        return

    JacobiMethod(matrix, vector, epsilon, next_guess, counter + 1)

def GaussSeidelMethod(matrix, vector, epsilon, previous, counter):
    """
    Function for solving a set of equations according to the GaussSeidel method
    :param matrix: Matrix nxn
    :param vector: Vector n
    :param epsilon: Stop Conditions
    :param previous: Result vector
    :param counter: Number of iterations
    """
    next_guess = previous.copy()
    for i in range(len(matrix)):
        ins = 0
        for j in range(len(matrix)):
            if i != j:
                ins += matrix[i][j] * next_guess[j]
        next_guess[i] = 1 / matrix[i][i] * (vector[i] - ins)

    print(f"Iteration no. {counter} {next_guess.tolist()}")

    if np.linalg.norm(next_guess - previous, ord=np.inf) < epsilon:
        return

    GaussSeidelMethod(matrix, vector, epsilon, next_guess, counter + 1)

matrixA = np.array([[4, 2, 0], [2, 10, 4], [0, 4, 5]])
b = np.array([2, 6, 5])
epsilon = 0.001

if CheckDominantDiagonal(matrixA):
    print("There is a dominant diagonal.")
    D, L, U = matrixDLUdissasembly(matrixA)
    print("\nMatrix D:")
    print(D)
    print("\nMatrix L:")
    print(L)
    print("\nMatrix U:")
    print(U)
    
    print("\n~~~ Jacobi Method ~~~\n")
    JacobiMethod(matrixA, b, epsilon, np.zeros(len(b)), 1)
    
    print("\n~~~ Gauss-Seidel Method ~~~\n")
    GaussSeidelMethod(matrixA, b, epsilon, np.zeros(len(b)), 1)
else:
    print("The matrix does not have a dominant diagonal.")
