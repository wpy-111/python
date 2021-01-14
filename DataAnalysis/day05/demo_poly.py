"""
    多项式
"""
import numpy as np
import matplotlib.pyplot as mp

P = [4,3,-1000,1]
x = np.linspace(-20,20,1000)
y = np.polyval(P,x)
#求导 ，然后求导函数的跟
Q = np.polyder(P)
xs = np.roots(Q)
ys = np.polyval(P,xs)

mp.scatter(xs,ys,s=80,color='orangered',zorder=3,marker='D')


mp.plot(x,y)
mp.grid(linestyle=':')
mp.show()
