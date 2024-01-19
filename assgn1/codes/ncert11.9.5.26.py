import numpy as np 
import matplotlib.pyplot as plt 

# Define the functions

# For x_1(n)
def func1(n):
    return np.where(n >= 0, ((n + 1) * (n + 2)**2), 0)

# For x_2(n)
def func2(n):
    return np.where(n >= 0, ((n + 1)**2 * (n + 2)), 0)

# For y_1(n)
def func3(n):
    return np.where(n >= 0, (3*n**4 + 26*n**3 + 81*n**2 + 106*n + 48) / 12, 0)

# For y_2(n)
def func4(n):
    return np.where(n >= 0, (3*n**4 + 22*n**3 + 57*n**2 + 62*n + 24) / 12, 0)

# Generate values for n to cover the range from -10 to 10 (inclusive) with a step of 1
n_values = np.arange(-10, 11, 1)

# Generate, save, and clear each plot

# Plot 1
plt.stem(n_values, func1(n_values), label=r'$(n+1)(n +2)^2$')
plt.legend()
plt.xlabel("n")
plt.ylabel("x_1(n)")
plt.title("Stem plot of x_1(n)")
plt.savefig("x1_plot.png")
plt.clf()  # Clear the figure

# Plot 2
plt.stem(n_values, func2(n_values), label=r'$(n+1)^2(n +2)$')
plt.legend()
plt.xlabel("n")
plt.ylabel("x_2(n)")
plt.title("Stem plot of x_2(n)")
plt.savefig("x2_plot.png")
plt.clf()

# Plot 3
plt.stem(n_values, func3(n_values), label=r'$\frac{3n^4+26n^3+81n^2+106n+48}{12}$')
plt.legend()
plt.xlabel("n")
plt.ylabel("y_1(n)")
plt.title("Stem plot of y_1(n)")
plt.savefig("y1_plot.png")
plt.clf()

# Plot 4
plt.stem(n_values, func4(n_values), label=r'$\frac{3n^4+22n^3+57n^2+62n+24}{12}$')
plt.legend()
plt.xlabel("n")
plt.ylabel("y_2(n)")
plt.title("Stem plot of y_2(n)")
plt.savefig("y2_plot.png")
plt.clf()


