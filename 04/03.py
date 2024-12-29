import numpy as np
import matplotlib.pyplot as plt

N = 64
Nb = 0
Ne = N
n = np.arange(Nb, Ne + 1)

# Signal X1[n] = cos(alpha1 * n)
alpha1 = 1 * (2 * np.pi / N)
x1 = np.cos(alpha1 * n)
fig1 = plt.figure()
ax1 = fig1.add_subplot(6, 1, 3)
ax1.stem(n, x1)
ax1.set_xlabel("Time $n$")
ax1.set_ylabel("$x[n]$")

# Signal X2[n] = cos(alpha2 * n)
alpha2 = 2 * (2 * np.pi / N)
x2 = np.cos(alpha2 * n)
ax1 = fig1.add_subplot(6, 1, 4)
ax1.stem(n, x2)
ax1.set_xlabel("Time $n$")
ax1.set_ylabel("$x[n]$")

# Signal X3[n] = cos(5 * alpha1 * n)
alpha3 = 5 * (2 * np.pi / N)
x3 = np.cos(alpha3 * n)
ax1 = fig1.add_subplot(6, 1, 5)
ax1.stem(n, x3)
ax1.set_xlabel("Time $n$")
ax1.set_ylabel("$x[n]$")

plt.show()
