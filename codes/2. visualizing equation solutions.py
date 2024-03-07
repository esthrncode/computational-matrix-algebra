#Solve & Plot the equation:
#- \( -x + 3y = 1 \)
#- \( 2x - 4y = -4 \)

import numpy as np
import matplotlib.pyplot as plt

# Define the equations as functions
def line1(x):
    return (1 + x) / 3

def line2(x):
    return (2*x + 4) / 4

# Create an array of x values
x_values = np.linspace(-10, 10, 400)

# Plot the lines
plt.plot(x_values, line1(x_values), label='-x + 3y = 1')
plt.plot(x_values, line2(x_values), label='2x - 4y = -4')

# Solve the system of equations to find the intersection point
A = np.array([[1, -3], [2, 4]])
b = np.array([-1, -4])
solution = np.linalg.solve(A, b)

# Plot the solution
plt.plot(solution[0], solution[1], 'ro') # red dot

# Set plot limits and add labels and legend
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()

# Display the plot
plt.show()

