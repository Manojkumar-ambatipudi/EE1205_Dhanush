import matplotlib.pyplot as plt
import numpy as np

# Define the function
def temp_function(n):
    return (n * (n + 1) * (n + 2) * (3 * n + 5)) / 12

# Generate values for n
n_values = np.arange(0, 10, 1)

# Calculate corresponding function values
y_values = temp_function(n_values)

# Plot the stem plot
plt.stem(n_values, y_values, linefmt='-', markerfmt='o', basefmt='r', label=r'$\frac{n(n + 1)(n + 2)(3n + 5)}{12}$')
plt.xlabel('n')
plt.ylabel('x[n]')
plt.title('Stem Plot of the Expression')
plt.legend()
plt.grid(True)
plt.show()
