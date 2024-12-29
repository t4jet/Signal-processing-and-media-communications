# importing mplot3d toolkits, numpy and matplotlib
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

ax = plt.axes(projection ='3d')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

# Defining all 3 axes
z = 0
x = np.linspace(0, 2*np.pi, 36) #create 36 linear data.
y = 5*np.sin(x)

print(x)
print(y)
print(z)

ax.scatter3D(x,y,z)
ax.plot3D(x, y, z, 'green') #please try this, too.
ax.set_title('3D line scatter & line plot')
plt.show()

