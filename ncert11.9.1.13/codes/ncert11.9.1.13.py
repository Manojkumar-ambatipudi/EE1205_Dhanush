import numpy as np
import matplotlib.pyplot as plt

# Read data from the file using numpy
data_file = "output_data.txt"
data = np.loadtxt(data_file, skiprows=1)  # Skip the header

# Extract columns
n_values = data[:, 0]
x_values = data[:, 1]

#close all the previous figs
plt.close("all")

# Plot the data using matplotlib
plt.stem(n_values, x_values, basefmt=" ", linefmt="-", markerfmt="o")
plt.xlabel('n')
plt.ylabel('x(n)')
plt.title('Plot of x(n)')
plt.grid(True)
plt.savefig("fig_x(n).png")
