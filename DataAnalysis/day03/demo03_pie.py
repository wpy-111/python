"""
  饼状图
"""
import matplotlib.pyplot as mp
import numpy as np

mp.figure('PieChart', facecolor='lightgray')
mp.title('PieChart', fontsize=20)
# 整理数据
values = [15, 13.3, 8.5, 7.3, 4.62, 51.28]
spaces = [0.05, 0.01, 0.01, 0.01, 0.01, 0.01]
labels = ['Java', 'C', 'Python', 'C++', 'VB', 'Other']
colors = ['dodgerblue', 'orangered', 'limegreen', 'violet', 'gold','blue']
mp.pie(values,spaces,labels,colors,'%.1f%%',shadow=True,startangle=0,radius=1)
#设置等轴比例
mp.axis('equal')
mp.legend()
mp.show()