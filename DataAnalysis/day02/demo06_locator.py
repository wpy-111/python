"""
    刻度定位器  enumerate 枚举函数 迭代返回下标和内容
"""
import matplotlib.pyplot as mp
mp.figure('Locators',facecolor='lightgrey')
ax = mp.gca()
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['left'].set_color('none')
ax.spines['bottom'].set_position(('data',0.5))
#设置x轴的数值区间
mp.xlim(1,10)
mp.ylim(-5,5)
#设置刻度定位器
ax.xaxis.set_major_locator(mp.MultipleLocator(1))
ax.xaxis.set_minor_locator(mp.MultipleLocator(0.1))
ax.yaxis.set_major_locator(mp.MultipleLocator(1))
ax.yaxis.set_minor_locator(mp.MultipleLocator(0.5))


mp.show()


