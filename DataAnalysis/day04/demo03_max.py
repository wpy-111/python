"""
   最值
"""
import numpy as np
import matplotlib.pyplot as mp
import datetime as dt
def dmy2ymd(dmy):
    dmy = str(dmy, encoding="utf-8")
    # 从指定字符串返回一个日期时间对象
    dat = dt.datetime.strptime(dmy, "%d-%m-%Y").date()
    tm = dat.strftime("%Y-%m-%d")  # 格式化
    return tm
datas,opening_prices,highest_prices,lowest_prices,closing_prices,volumes = \
    np.loadtxt('aapl.csv',delimiter=',',usecols=(1,3,4,5,6,7),
           dtype=('M8[D],f8,f8,f8,f8,f8'),unpack=True,converters={1:dmy2ymd})
max_val = np.max(highest_prices)
min_val = np.min(lowest_prices)
print(max_val,'~',min_val)
#获取最大值和最小值的下标
max_ind = np.argmax(highest_prices)
min_ind = np.argmin(lowest_prices)
print(max_ind,'~',min_ind)
print(datas[max_ind],datas[min_ind])

#maximum minimum
a = np.arange(1,10).reshape(3,3)
b = np.arange(1,10)[::-1].reshape(3,3)
print(a)
print(b)
print(np.maximum(a,b))
print(np.minimum(a,b))







