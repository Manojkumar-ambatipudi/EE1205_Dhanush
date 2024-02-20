import numpy as np
import matplotlib.pyplot as plt

from fft_algo import *

from ifft_algo import *

def cross_corelation(x,y):
    X = FFT(x)
    Y = FFT(y)

    result_in_freq_domain = X * np.conj(Y)

    result = IFFT(result_in_freq_domain)
    return result





x = np.array([1, 1/np.sqrt(2), 0, -1/np.sqrt(2), -1, -1/np.sqrt(2), 0, 1/np.sqrt(2)])
y = np.roll(x, shift=1)  # y(n) = x(n + 1)

r_xy = cross_corelation(x,y)
plt.stem(r_xy.real,label='r_xy(k)')

# Mark the value of r_xy at k=0 with a cross
plt.scatter(0, r_xy.real[0], marker='x', s=100 , color='red', label=f'r_xy(0)={r_xy.real[0]:.4f}')
plt.title('Cross-Correlation using DFT')

plt.xlabel('k')
plt.ylabel('r_xy')
plt.grid(True)
plt.legend()
plt.savefig("cross-corelation.png")

