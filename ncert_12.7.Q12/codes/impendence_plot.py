import numpy as np
import matplotlib.pyplot as plt

# Given values for LC circuit
L = 50e-6  # Inductance in Henry (50 uH)
C = 50e-6  # Capacitance in Farad (50 uF)

# Generate frequency values up to 4000 Hz
frequencies = np.linspace(1, 4000, 400)  # Adjust the number of points as needed

# Calculate impedance for the LC circuit
impedance = 2 * np.pi * frequencies * L - 1 / (2 * np.pi * frequencies * C)

# Find the natural frequency
natural_frequency = 1 / (2 * np.pi * np.sqrt(L * C))

# Find the frequency at which minimum impedance occurs
min_impedance_frequency = frequencies[np.argmin(np.abs(impedance))]


plt.clf()
# Plotting |Z| vs f with log scale for y-axis
plt.figure(figsize=(8, 6))
plt.plot(frequencies, np.abs(impedance), label='|Z| vs f', linestyle='-', color='blue', linewidth=2)

# Mark the natural frequency on the plot
natural_frequency_index = np.argmin(np.abs(frequencies - natural_frequency))
plt.scatter(natural_frequency, np.abs(impedance[natural_frequency_index]), color='red', s=100, label='Natural Frequency')

# Annotate the value at the marked natural frequency
plt.text(natural_frequency, np.abs(impedance[natural_frequency_index]), f'({natural_frequency:.2f} Hz)',
         color='black', fontsize=10, ha='right', va='bottom')

plt.xlabel('Frequency (Hz)')
plt.ylabel('|Z| (Impedance Magnitude) - Log Scale')
plt.title('Impedance Magnitude vs Frequency for LC Circuit ')
plt.legend(loc='upper right')
plt.grid(True)
plt.yscale('log')  # Set log scale for the y-axis

plt.savefig("impedance_plot.png")



