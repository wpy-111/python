"""
    dateframe
"""
import numpy as np
import pandas as pd
data = [['Alex',10],['Bob',12],['Clarke',14]]
df = pd.DataFrame(data)
date = [{'a': 1, 'b': 2}]
print(df)
print(pd.DataFrame(date))
df = pd.DataFrame(data,index=['AID01','AID02','AID03'],columns=['Name','Age'])
print(df)
print('=========================================')
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data, index=['s1','s2','s3','s4'])
print(df)
print('*'*50)
data = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
        'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(data)
print(df[['one','two']])
#dataframe列添加
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data,index=['AID01','AID02','AID03','AID04',])
df['score'] = pd.Series([80,98,99,85],index=['AID01','AID02','AID03','AID04',])
print(df)
print('*'*50)
#列的删除
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
     'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd']),
     'three' : pd.Series([10, 20, 30], index=['a', 'b', 'c'])}
df = pd.DataFrame(d)
print("dataframe is:")
print(df)
df.pop('one')
print(df)
del(df['two'])
print(df)
print('===*'*20)
#行访问 loc名字 iloc数字
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
    'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd']),
    'three': pd.Series([10, 20, 30], index=['a', 'b', 'c'])}
df = pd.DataFrame(d)
print(df)
print('--------------------------------------')
print(df[1:3])
print('--------------------------------------')
print(df.iloc[[0,1]])
print('--------------------------------------')
print(df.loc[['a','b']])
print('==================================================')
#行添加 索引可以重复
df = pd.DataFrame([['zs', 12], ['ls', 4]], index=[0, 1], columns = ['Name','Age'])
df2 = pd.DataFrame([['ww', 16], ['zl', 8]], index=[5, 6], columns = ['Name','Age'])
df = df.append(df2)
print(df)
#行删除 只能是索引名
df = df.drop([0,5])
print(df)
print('-'*100)
#测试代码
data = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(data,index=['a','b','c']) #key为index， value为value
print(s)
print('==================================================')
#数据修改
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
    'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd']),
    'three': pd.Series([10, 20, 30], index=['a', 'b', 'c'])}
df = pd.DataFrame(d)
df['one']['a'] = 99
print(df)
