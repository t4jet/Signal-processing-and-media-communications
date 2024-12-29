import numpy as np #pip install numpy
import matplotlib.pyplot as plt #pip install matplotlib

N=64
#Nb=-N//4;Ne=N+N//4
Nb=0;Ne=N
n=np.arange(Nb,Ne+1)

#信号直流成分a0
A0=5
a0 = A0*np.ones(N+1)
fig1=plt.figure()
ax1=fig1.add_subplot(7,1,3)
ax1.stem(n,a0)
#ax1.set_xlim(Nb,Ne);ax1.set_ylim(-2,2);ax1.grid()
ax1.set_xlabel("Time $n$")
ax1.set_ylabel("$a[0]$")

#信号a1
alpha1 = 1*(2*np.pi/N)
A1=13
a1 = A1*np.cos(alpha1*n)
#fig1=plt.figure()
ax1=fig1.add_subplot(7,1,4)
ax1.stem(n,a1)
#ax1.set_xlim(Nb,Ne);ax1.set_ylim(-2,2);ax1.grid()
ax1.set_xlabel("Time $n$")
ax1.set_ylabel("$a[1]$")

alpha2 = 2*(2*np.pi/N)
A2=3
a2 = A2*np.cos(alpha2*n)
#fig1=plt.figure()
ax1=fig1.add_subplot(7,1,5)
ax1.stem(n,a2)
#ax1.set_xlim(Nb,Ne);ax1.set_ylim(-2,2);ax1.grid()
ax1.set_xlabel("Time $n$")
ax1.set_ylabel("$a[2]$")


ax1=fig1.add_subplot(7,1,6)
alpha1= 1*(2*np.pi/N)
B1=4
b1 = B1*np.sin(alpha1*n)
ax1.stem(n,b1)
#ax1.set_xlim(Nb,Ne);ax1.set_ylim(-2,2);ax1.grid()
ax1.set_xlabel("Time $n$")
ax1.set_ylabel("$b[1]$")

ax1=fig1.add_subplot(7,1,7)
alpha2= 2*(2*np.pi/N)
B2=20
b2 = B2*np.sin(alpha2*n)
ax1.stem(n,b2)
#ax1.set_xlim(Nb,Ne);ax1.set_ylim(-2,2);ax1.grid()
ax1.set_xlabel("Time $n$")
ax1.set_ylabel("$b[2]$")

ax1=fig1.add_subplot(7,1,1)
ft = a0+a1+a2+b1+b2
ax1.stem(n,ft)
#ax1.set_xlim(Nb,Ne);ax1.set_ylim(-2,2);ax1.grid()
ax1.set_xlabel("Time $n$")
ax1.set_ylabel("$f(t)]$")

#----------------------------------
#----------------------------------
#----------------------------------
#----------------------------------

fig2=plt.figure()
ax1=fig2.add_subplot(7,5,1)
ax1.stem(n,ft)
#ax1.set_xlim(Nb,Ne);ax1.set_ylim(-2,2);ax1.grid()
ax1.set_xlabel("Time $n$")
ax1.set_ylabel("$f(t)$")

alpha1 = 1*(2*np.pi/N)
c1 = np.cos(alpha1*n)
ax1=fig2.add_subplot(7,5,6)
ax1.stem(n,c1)
#ax1.set_xlim(Nb,Ne);ax1.set_ylim(-2,2);ax1.grid()
ax1.set_xlabel("Time $n$")
ax1.set_ylabel("$1*cos(1wt)$")

ax1=fig2.add_subplot(6,5,2)
ax1.stem(n,a1)
#ax1.set_xlim(Nb,Ne);ax1.set_ylim(-2,2);ax1.grid()
ax1.set_xlabel("Time $n$")
ax1.set_ylabel("$a1$")

ax1=fig2.add_subplot(6,5,7)
c1 = np.cos(alpha1*n)
ax1.stem(n,c1)
#ax1.set_xlim(Nb,Ne);ax1.set_ylim(-2,2);ax1.grid()
ax1.set_xlabel("Time $n$")
ax1.set_ylabel("$1*cos(1wt)$")

ax1=fig2.add_subplot(6,5,12+5)
ax1.stem(n,a1*c1)
#ax1.set_xlim(Nb,Ne);ax1.set_ylim(-2,2);ax1.grid()
ax1.set_xlabel("Time $n$")
ax1.set_ylabel("$a1*cos(1wt)$")


ax1=fig2.add_subplot(6,5,3)
ax1.stem(n,b1)
#ax1.set_xlim(Nb,Ne);ax1.set_ylim(-2,2);ax1.grid()
ax1.set_xlabel("Time $n$")
ax1.set_ylabel("$b1$")

ax1=fig2.add_subplot(6,5,13+5)
ax1.stem(n,b1*c1)
#ax1.set_xlim(Nb,Ne);ax1.set_ylim(-2,2);ax1.grid()
ax1.set_xlabel("Time $n$")
ax1.set_ylabel("$b1*cos(1wt)$")

ax1=fig2.add_subplot(6,5,9)
c1 = np.cos(alpha1*n)
ax1.stem(n,c1)
#ax1.set_xlim(Nb,Ne);ax1.set_ylim(-2,2);ax1.grid()
ax1.set_xlabel("Time $n$")
ax1.set_ylabel("$1*cos(1wt)$")

ax1=fig2.add_subplot(6,5,14+5)
ax1.stem(n,a2*c1)
#ax1.set_xlim(Nb,Ne);ax1.set_ylim(-2,2);ax1.grid()
ax1.set_xlabel("Time $n$")
ax1.set_ylabel("$a2*cos(1wt)$")

ax1=fig2.add_subplot(6,5,5)
ax1.stem(n,b2)
#ax1.set_xlim(Nb,Ne);ax1.set_ylim(-2,2);ax1.grid()
ax1.set_xlabel("Time $n$")
ax1.set_ylabel("$b2$")

ax1=fig2.add_subplot(6,5,10)
c1 = np.cos(alpha1*n)
ax1.stem(n,c1)
#ax1.set_xlim(Nb,Ne);ax1.set_ylim(-2,2);ax1.grid()
ax1.set_xlabel("Time $n$")
ax1.set_ylabel("$1*cos(1wt)$")

ax1=fig2.add_subplot(6,5,12+5)
ax1.stem(n,a1*c1)
ax1.set_xlabel("Time $n$")
ax1.set_ylabel("$a1 \\cdot cos(1wt)$")


plt.show()


