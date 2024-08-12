"""
GitHub Repo:
https://github.com/EvgeniBursov/NumericalAnalysis/tree/main/Ex4

Evgeni Bursov
Yael Berko
"""

import math
import numpy as np

def LinearInterpolation(table_points, point):
    result = None
    for i in range(len(table_points) - 1):
        x1, y1 = table_points[i]
        x2, y2 = table_points[i + 1]
        
        if x1 <= point <= x2:
            result = (((y1 - y2) / (x1 - x2)) * point) + ((y2 * x1) - (y1 * x2)) / (x1 - x2)
            print(f"The liniear interpolation of the point {point} is: {round(result, 4)}")
            break
    
    if result is None:
        x1, y1 = table_points[0]
        x2, y2 = table_points[1]
        m = (y1 - y2) / (x1 - x2)
        result = y1 + m * (point - x1)
        print(f"The liniear extrapolation of the point {point} is: {round(result, 4)}")


def PolynomialInterpolation(table_points, point):
    i = 0
    matrix = []
    resvec = []
    while i < len(table_points):
        lineToAppend = []
        for j in range(len(table_points)):
            lineToAppend.append(math.pow(table_points[i][0], j))
        matrix.append(lineToAppend)
        resvec.append(table_points[i][1])
        i += 1
    matrix = np.array(matrix)
    resvec = np.array(resvec)
    prefixValues = np.linalg.solve(matrix, resvec)
    result = 0
    for i in range(len(prefixValues)):
        result += math.pow(point, i) * prefixValues[i]
    print(f"The polynomial extrapolation of the point {point} is: {round(result, 4)}")


def LagrangeMethod(table_points, point):
    xp = []
    yp = []
    result = 0
    for i in range(len(table_points)):
        xp.append(table_points[i][0])
        yp.append(table_points[i][1])
    for i in range(len(table_points)):
        lagrange_i = 1
        for j in range(len(table_points)):
            if i != j:
                lagrange_i = lagrange_i * (point - xp[j]) / (xp[i] - xp[j])
        result += lagrange_i * yp[i]
    print(f"The approximation (interpolation) of the point {point} is: {round(result, 4)}")


def choose_interpolation_method(table_points, x_value):
    print("Choose the interpolation method:")
    print("1: Linear Interpolation")
    print("2: Polynomial Interpolation")
    print("3: Lagrange Method")
    
    method_choice = input()
    
    if method_choice == "1":
        return LinearInterpolation(table_points, x_value)
    elif method_choice == "2":
        return PolynomialInterpolation(table_points, x_value)
    elif method_choice == "3":
        return LagrangeMethod(table_points, x_value)
    else:
        print("Wrong option")
        return None


if __name__ == '__main__':
    table_points1 = [(1, 0.8415),(2, 0.9093),(3, 0.1411)]
    x = 2.5

    table_points2 = [(2, 0.9093),(3, 0.1411),(4, -0.7568)]
    y = 3.5

    table_points3 = [(4, -0.7568),(5, -0.9589),(6,-0.2794)]
    z = 4.5


    while True:
        print("Choose the x and the points to calculate:")
        print("1: Points", table_points1, "x:", x)
        print("2: Points", table_points2, "x:", y)
        print("3: Points", table_points3, "x:", z)
        
        choice = input()

        if choice == "1":
            choose_interpolation_method(table_points1, x)
        elif choice == "2":
            choose_interpolation_method(table_points2, y)
        elif choice == "3":
            choose_interpolation_method(table_points3, z)
        else:
            print("Wrong option")
