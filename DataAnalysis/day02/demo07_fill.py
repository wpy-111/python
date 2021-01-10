"""
    填充
"""
import matplotlib.pyplot as mp
import numpy as np

x = np.linspace(0,8*np.pi,1000)
sinx = np.sin(x)
cosx = np.cos(x / 2) / 2
mp.figure("Fill",facecolor='lightgrey')
mp.title('Fill',fontsize=16)
mp.grid(linestyle=':')
mp.plot(x,sinx,linestyle='-',linewidth=2,color='blue',alpha=0.8,label=r'$y=sin(x)$')
mp.plot(x,cosx,linestyle='-',linewidth=2,color='orangered',alpha=0.8,label=r'$y=\frac{cos(\frac{x}{2})}{2}$')
#填充
mp.fill_between(x,sinx,cosx,sinx>cosx,color='dodgerblue',alpha=0.3)
mp.fill_between(x,sinx,cosx,sinx<cosx,color='orangered',alpha=0.3)

mp.legend()
mp.show()







