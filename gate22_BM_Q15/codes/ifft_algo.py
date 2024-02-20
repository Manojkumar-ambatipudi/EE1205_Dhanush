import numpy as np

def IFFT(X):
    N = len(X)

    if N == 1:
        return X
    else:
        X_even = IFFT(X[::2])
        X_odd = IFFT(X[1::2])
        factor = np.exp(2j * np.pi * np.arange(N) / N)

        x = np.concatenate(
            [X_even + factor[:int(N / 2)] * X_odd,
             X_even + factor[int(N / 2):] * X_odd]) / 2
        return x