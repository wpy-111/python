"""
   散点图
"""
import numpy as np
import matplotlib.pyplot as mp
n = 200
#175是数学期望，5标准差，n是数量
x = np.random.normal(175,5,n)
y = np.random.normal(60,10,n)
mp.figure('Scatter',facecolor='lightgrey')
mp.title("Scatter",fontsize=16)
mp.grid(linestyle=':')
mp.xlabel('Height',fontsize=14)
mp.ylabel('Weight',fontsize=14)
#c=数字，这个数字越小越接近蓝色，越大越接近红色 cmap='jet'设置点的颜色给每个点
#越靠近d数越小（蓝色），越远离d数越大（红色）
#jet从蓝到红
#brg 蓝-红-绿
#rainbow 赤橙蓝绿青蓝紫
#gray 黑到白
#加_r颜色相反
d = (x-175)**2+(y-60)**2
mp.scatter(x,y,s=80,alpha=0.8,label='Persons',c=d,cmap='gray_r')
mp.legend()
mp.show()






