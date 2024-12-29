import numpy as np
import matplotlib.pyplot as plt

nbegin = -5;nend = 10
n = np.array([-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10])

delta = np.array([0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0])
fig1 = plt.figure()
ax1 = fig1.add_subplot(1,1,1)
ax1.stem(n, delta)
ax1.set_xlim(nbegin, nend); ax1.set_ylim(-0.2, 1.2); ax1.grid()
ax1.set_xlabel('Time $n$'); ax1.set_ylabel('$\delta[n]$')

unitstep = np.array([0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1])
fig2 = plt.figure()
ax2 = fig2.add_subplot(1,1,1)
ax2.stem(n, unitstep)
ax2.set_xlim(nbegin, nend); ax2.set_ylim(-0.2,1.2); ax2.grid()
ax2.set_xlabel('Time $n$'); ax2.set_ylabel('$u_0[n]$')
plt.show()