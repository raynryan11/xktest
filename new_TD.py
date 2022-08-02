import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5, 5, 0.1)   # 定义域-5~5
y = x**2   # 求解的函数
pointx = []    # 用来储存每次梯度下降后的点
x0 = -0.1      # 初始值的横坐标-2，随便选的
pointx.append(x0)

lr = 1.2

for i in range(15):   # 先执行10次
    xnew = x0-lr*2*x0   # 该点减去该点的导数值
    x0 = xnew   # 移动到新的点
    pointx.append(x0)   # 储存点运动轨迹

pointy = np.array(pointx)**2
plt.plot(x, y, 'g')   # 画函数图像
plt.plot(pointx, pointy, 'r')   # 画梯度轨迹
plt.show()
