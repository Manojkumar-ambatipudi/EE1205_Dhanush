import matplotlib.pyplot as plt
import numpy as np

# Define the function 
def temp_function(n):
    return np.where(n >= 0, n**3 + 5 * n**2 + 20 * n + 4, 0)

# Generate values for n to cover the range from -10 to 10 (inclusive) with a step of 1
n_values = np.arange(-10, 11, 1)

# Calculate corresponding function values
y_values = temp_function(n_values)

# Plot the stem plot without connecting lines
plt.stem(n_values, y_values, linefmt='', markerfmt='o', basefmt='r', label=r'$n^3+5n^2+20n+4$')
plt.xlabel('n')
plt.ylabel('x_1(n)')
plt.title('Stem Plot of the Expression')

# Set y-axis limits from 0 to max(y_values)
plt.ylim(bottom=0, top=max(y_values))

# Set y-axis ticks with a gap of 250
plt.yticks(np.arange(0, max(y_values) + 250, 250))

# Draw the x-axis at y=0
plt.axhline(0, color='black', linestyle='--', linewidth=0.8)

# Move the legend to the left side
plt.legend(loc='upper left')

plt.grid(True)
plt.show()
# the below line of code can be used to save figure in the same directory 
# plt.savefig("11_9_5_26_1.png")