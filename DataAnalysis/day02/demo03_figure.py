"""
   demo03_figure.py 窗口操作
"""
import numbers as np
import matplotlib.pyplot as mp

mp.figure('FigureA',facecolor='grey')
mp.plot([1,2],[2,1],linestyle='--',linewidth=2,color='red')
mp.figure('FigureB',facecolor='lightgrey')
mp.plot([1,2],[2,1],linestyle='-.',linewidth=3,color='blue')
#测试窗口常用参数
mp.title('Figure B ',fontsize=16)
mp.xlabel('X',fontsize=14)#x轴的标注
mp.ylabel('Y',fontsize=14)#y轴的标注
#设置网格线
mp.grid(linestyle=':')
mp.tight_layout()
mp.show()