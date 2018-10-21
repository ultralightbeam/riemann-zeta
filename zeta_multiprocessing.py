"""Plot some riemann-zeta with multiprocessing
"""

import numpy as np
import matplotlib.pyplot as plt
from mpmath import zeta
from multiprocessing import Pool

limval_real = 5
limval_imag = 30
nval = 100

v_real = np.linspace(-limval_real, limval_real, nval)
v_imag = np.linspace(-limval_imag, limval_imag, nval)

def get_zeta(w):
	"""
		Input:
			v: triplet of zeta input, real ind, imag ind
	"""
	M = np.zeros((nval, nval)) + 1j * np.zeros((nval, nval))
	M[w[2], w[1]] = zeta(w[0])
	return M

def main():
	v = []
	for i in range(len(v_real)):
		for j in range(len(v_imag)):
			x = v_real[i] + 1j * v_imag[j]
			v.append([x, i, j])
	p = Pool(8)
	m = p.map(get_zeta, v)
	M = sum(m)
	plt.figure
	plt.pcolormesh(v_real, v_imag, np.absolute(M))
	plt.clim([0, 1])
	plt.colorbar()
	plt.show()

if __name__ == '__main__':
	main()
