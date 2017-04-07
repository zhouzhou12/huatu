'''
画三维散点图
4a.mat数据从以下网址下载：http://blog.csdn.net/Eddy_zheng/article/details/50496194
'''

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import  scipy.io as sio

mat=sio.loadmat('4a.mat')
data=mat['data']
x,y,z=data[0],data[1],data[2]
ax=plt.subplot(111,projection='3d')#创建一个三维的绘图工程
#将数据点分成三部分画，在颜色上有区分度
ax.scatter(x[:1500],y[:1500],z[:1500],c='y')
ax.scatter(x[1500:5000],y[1500:5000],z[1500:5000],c='r')
ax.scatter(x[5000:],y[5000:],z[5000:],color='g')

ax.set_zlabel('Z') #坐标轴
ax.set_ylabel('Y')
ax.set_xlabel('X')

plt.savefig('4a.jpg')
plt.show()
