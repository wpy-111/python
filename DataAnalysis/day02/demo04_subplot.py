"""
    demo04_subplot.py  子图
"""
import matplotlib.pyplot as mp
mp.figure('Subplot',facecolor='lightgrey')
for i in range(1,10):
    mp.subplot(3,3,i)
    mp.text(0.5,0.5,i,ha='center',va='center',size=36)
    mp.xticks([])
    mp.yticks([])
    mp.tight_layout()
mp.show()