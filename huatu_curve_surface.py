'''
画曲面图
'''
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x=np.arange(-9,9,0.3)
y=np.arange(-6,6,0.2)
x,y=np.meshgrid(x,y)

z=(x**2/9.0+y**2/4.0)/2.0

fig=plt.figure()
ax=Axes3D(fig)
ax.plot_surface(x,y,z,rstride=1,cstride=1,cmap='rainbow')

plt.savefig('椭圆抛物面.jpg')

z=(x**2/9.0-y**2/4.0)/2.0

fig=plt.figure()
ax=Axes3D(fig)
ax.plot_surface(x,y,z,rstride=1,cstride=1,cmap='rainbow')
plt.savefig('双曲抛物面.jpg')
plt.show()
