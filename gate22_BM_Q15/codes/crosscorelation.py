import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, ifft

def cross_correlation_dft(x, y):
    
    # Compute the DFT of x(n) and y(n)
    X = fft(x)
    Y = fft(y)
    
    # Compute the cross-correlation in the frequency domain
    result_freq_domain = X * np.conj(Y)
    
    # Compute the inverse DFT to get the time-domain cross-correlation
    result = ifft(result_freq_domain)
    
    return result

# Example signals
x = np.array([1, 1/np.sqrt(2), 0, -1/np.sqrt(2), -1, -1/np.sqrt(2), 0, 1/np.sqrt(2)])
y = np.roll(x, shift=1)  # y(n) = x(n + 1)

# Calculate cross-correlation using DFT
result_dft = cross_correlation_dft(x, y)

# Plot the real part of the result
plt.stem(result_dft.real,label='r_xy(k)')

# Mark the value of r_xy at k=0 with a cross
plt.scatter(0, result_dft[0], marker='x', s=100 , color='red', label=f'r_xy(0)={result_dft[0]:.4f}')
plt.title('Cross-Correlation using DFT')

plt.xlabel('k')
plt.ylabel('r_xy')
plt.grid(True)
plt.legend()
plt.savefig("cross-corelation.png")

