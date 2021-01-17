"""

"""
import pandas as pd
import numpy as np
dates = pd.Series(['2011', '2011-02', '2011-03-01', '2011/04/01',
                   '2011/05/01 01:01:01', '01 Jun 2011'])
dates = pd.to_datetime(dates)
print(dates)
print(dates.dt.dayofyear)
#datetimeindex 使用日期类型最为数据元素的索引
data = [20,30,40,50,66,15,25]
s = pd.Series(data,index=pd.date_range('2020/03/10',periods=7))
print(s)
print(s[:3])
print('---------------------------------------')
times = pd.date_range('2020-3-10',periods=7,freq='D')
print(times)
times = pd.date_range('2020-3-10',periods=7,freq='M')
print(times)
times = pd.date_range('2020-3-10',periods=7,freq='B')#B工作日周一到周五
print(times)
