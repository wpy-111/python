"""
    柱状图
"""
import numpy as np
import matplotlib.pyplot as mp

apples = np.array([82,45,62,48,55,44,69,88,15,21,36,58])
oranges = np.array([120,150,111,121,103,55,95,65,48,52,99,88])
mp.figure('Bar',facecolor='lightgrey')
mp.title("bar",fontsize=16)
mp.xlabel('Date',fontsize=14)
mp.ylabel('Volume',fontsize=14)
mp.grid(linestyle=':')
x = np.arange(apples.size)
mp.bar(x-0.2,apples,width=0.4,color='dodgerblue',label='Apples')
mp.bar(x+0.2,oranges,width=0.4,color='orangered',label='Oranges')
#修改x轴的刻度文本
mp.xticks(x,['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
mp.legend()
mp.show()