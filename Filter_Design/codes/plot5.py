import numpy as np
import matplotlib.pyplot as plt

# Define the piecewise function h_BP(n)
def h_BP(n):
    if n == 0:
        return 0.025 / np.pi
    elif -48 <= n <= 48:
        return (2 * np.cos(0.365 * n * np.pi) * np.sin(0.025 * n * np.pi)) / (n * np.pi)
    else:
        return 0

# Generate values for n
n_values = np.arange(-480, 491)

# Calculate h_BP values for each n
h_values = np.array([h_BP(n) for n in n_values])

# Calculate the DTFT using numpy's FFT
H_freq_response = np.fft.fftshift(np.fft.fft(h_values))

# Angular frequency axis (normalized)
omega_normalized = np.linspace(-np.pi, np.pi, len(n_values))

# Plotting
plt.plot(omega_normalized/np.pi, np.abs(H_freq_response))
plt.xlabel('($\omega$/pi)')
plt.ylabel('|H($\omega$)|')
plt.title('FIR BAND PASS FILTER')
plt.grid(True)
plt.savefig("FIR_Bandpass_Filter.png")
