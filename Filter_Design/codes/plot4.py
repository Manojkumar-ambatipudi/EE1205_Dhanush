import numpy as np
import matplotlib.pyplot as plt

# Define the piecewise function h_LP(n)
def h_LP(n):
    if n == 0:
        return 0.025 / np.pi
    elif -48 <= n <= 48:
        return (np.sin(0.025 * n * np.pi)) / (n * np.pi)
    else:
        return 0

# Generate values for n
n_values = np.arange(-480, 491)

# Calculate h_BP values for each n
h_values = np.array([h_LP(n) for n in n_values])

# Calculate the DTFT using numpy's FFT
H_freq_response = np.fft.fftshift(np.fft.fft(h_values))

# Angular frequency axis (normalized)
omega_normalized = np.linspace(-np.pi/2, np.pi/2, len(n_values))

# Plotting
plt.plot(omega_normalized/np.pi, np.abs(H_freq_response))
plt.xlabel('($\omega$/pi)')
plt.ylabel('|H(r$\omega$)|')
plt.title('FIR LOW PASS FILTER')
plt.grid(True)

plt.savefig("FIR_Low_Filter.png")
