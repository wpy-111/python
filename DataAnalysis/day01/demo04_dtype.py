"""
  demo04_dtype.py
"""
import numpy as np
ary = np.array([0,1,2,3,4],dtype='int32')
print(ary,ary.dtype)
ary = np.array([0,1,2,3,4],dtype='float64')
ary2 = ary.astype('int32')
print(ary,ary2.dtype)
ary = np.array([0,1,2,3,4],dtype='str')
print(ary,ary.dtype)

print('----------------------')
data=[
	('zs', [90, 80, 85], 15),
	('ls', [92, 81, 83], 16),
	('ww', [95, 85, 95], 15)
]
ary3 = np.array(data,dtype='U3,3int32,int32')
print(ary3,ary3.dtype)
print(ary3.shape)
print('-'*30)
ary3 = np.array(data,dtype=[('name','str',2),('score','int32',3),('age','int32',1)])
print(ary3)
print(ary3['score'])
print(ary3['name'])

print('='*30)
ary3 = np.array(data,dtype={'names':['name','score','age'],'formats':['U3','3int32','int32']})
print(ary3)
print(ary3['score'])
print(ary3['name'])

datestrs = np.array(['2011','2011-02','2011-03-01','2011-04-06 10:12:10'])
date = datestrs.astype('datetime64[D]')
print(date)
print(date[-1]-date[0])

