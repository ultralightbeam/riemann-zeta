
import numpy as np
import matplotlib.pyplot as plt
from mpmath import zeta

n_approx = 200


def main():
    limval = 20
    nval = 100

    v_real = np.linspace(-limval, limval, nval)
    v_imag = np.linspace(-limval, limval, nval)

    M = np.zeros((nval, nval)) + 1j * np.zeros((nval, nval))
    for i in range(len(v_real)):
        for j in range(len(v_imag)):
            x = v_real[i] + 1j * v_imag[j]
            M[j, i] = zeta(x)
            #M[j, i] = zeta(x)
    plt.figure
    plt.imshow(np.absolute(M), cmap='jet')
    plt.clim([0, 5])
    plt.colorbar()
    plt.show()


if __name__ == '__main__':
    main()
