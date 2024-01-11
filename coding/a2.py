import numpy as np 
import matplotlib.pyplot as plt
def u(n):
    return np.heaviside(n,1)
n = np.arange(0,10)
x_n = u(n) - u(n-6)
h_n = u(n)
y_n = u(n)
y_n = np.convolve(x_n , h_n ,mode='full')
plt.stem(range(len(y_n)) , y_n , use_line_collection = True)
plt.title("convolution of x(n) and h(n) " )
plt.savefig("other.png")
