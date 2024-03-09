# Practice Curve Fitting Example

import numpy as np
import matplotlib.pyplot as plt

def fitPoly3(p1, p2, p3, p4):
    # Create the matrix of powers of x
    A = np.array([
        [p1[0]**3, p1[0]**2, p1[0], 1],
        [p2[0]**3, p2[0]**2, p2[0], 1],
        [p3[0]**3, p3[0]**2, p3[0], 1],
        [p4[0]**3, p4[0]**2, p4[0], 1]
    ])
    
    # Create the vector of y values
    b = np.array([p1[1], p2[1], p3[1], p4[1]])

    # Solve the linear algebra system for the coefficients
    coeffs = np.linalg.solve(A, b)

    # Generate values for plotting
    x_values = np.linspace(-3, 3, 100)
    y_values = np.polyval(coeffs, x_values)

    # Plotting the polynomial and points
    plt.plot(x_values, y_values, label='Fitted Polynomial')
    plt.scatter([p1[0], p2[0], p3[0], p4[0]], [p1[1], p2[1], p3[1], p4[1]], color='red', label='Data Points')
    plt.title('Cubic Polynomial Fit')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.show()

    return coeffs

# Example data points
points = [(1, 2), (-1, 6), (2, 3), (3, 2)]

# Fitting the polynomial to the points
coefficients = fitPoly3(*points)
print("Cubic polynomial coefficients:", coefficients)
