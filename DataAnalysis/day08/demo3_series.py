"""
    series
"""
import numpy as np
import pandas as pd
#通过nddary创建series
s = pd.Series()
print(s,type(s))
ary = np.array(['zs','ls','ww','lz'])
s = pd.Series(ary)
print(s)
s = pd.Series(ary,index=['AID01','AID02','AID03','AID04'])
print(s,s['AID01'],s[0])
#通过字典创建series a,b,c 是索引
data = {'a':1001,'b':1001,'c':1003}
s = pd.Series(data)
print(s)
#从标量创建series
s = pd.Series(5,index=[0,1,2,3,4])
print(s)
#创建五十个1/5
s = pd.Series(1/5,index=np.arange(50))
print(s)


