import numpy as np
import matplotlib.pyplot as plt
 
N=64
#Nb=-N//4;Ne=N+N//4
Nb=0;Ne=N
n=np.arange(Nb,Ne+1)
 
#信号X[n]
alpha1 = 1*(2*np.pi/N)
x1 = np.cos(alpha1*n)
fig1=plt.figure()
ax1=fig1.add_subplot(6,1,3)
ax1.stem(n,x1)
#ax1.set_xlim(Nb,Ne);ax1.set_ylim(-2,2);ax1.grid()
ax1.set_xlabel("Time $n$")
ax1.set_ylabel("$x[n]$")

alpha2 = 2*(2*np.pi/N)
x2 = np.cos(alpha2*n)
#fig1=plt.figure()
ax1=fig1.add_subplot(6,1,4)
ax1.stem(n,x2)
#ax1.set_xlim(Nb,Ne);ax1.set_ylim(-2,2);ax1.grid()
ax1.set_xlabel("Time $n$")
ax1.set_ylabel("$x[n]$")

plt.show()