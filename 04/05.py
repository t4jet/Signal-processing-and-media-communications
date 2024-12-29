import numpy as np
import matplotlib.pyplot as plt

N = 64
Nb = 0
Ne = N
n = np.arange(Nb, Ne + 1)

# Complex signal f(t) = cos(alpha1 * n) + i * sin(alpha2 * n)
alpha1 = 1 * (2 * np.pi / N)
alpha2 = 2 * (2 * np.pi / N)
f = np.cos(alpha1 * n) + 1j * np.sin(alpha2 * n)

# Create a figure and add subplots
fig1 = plt.figure()

# 1st subplot (complex function)
ax1 = fig1.add_subplot(6, 1, 1)
ax1.plot(n, f.real, label='Real part', color='blue')
ax1.plot(n, f.imag, label='Imaginary part', color='red')
ax1.set_xlabel("Time $n$")
ax1.set_ylabel("$f[n]$")
ax1.legend()

# Signal X1[n] = cos(alpha1 * n)
x1 = np.cos(alpha1 * n)
ax1 = fig1.add_subplot(6, 1, 3)
ax1.stem(n, x1)
ax1.set_xlabel("Time $n$")
ax1.set_ylabel("$x[n]$")

# Signal X2[n] = cos(alpha2 * n)
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

# Signal X4[n] = cos(7 * alpha1 * n)
alpha4 = 7 * (2 * np.pi / N)
x4 = np.cos(alpha4 * n)
ax1 = fig1.add_subplot(6, 1, 6)
ax1.stem(n, x4)
ax1.set_xlabel("Time $n$")
ax1.set_ylabel("$x[n]$")

plt.show()
