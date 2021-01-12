"""
    pstd = np.std(close_prices)             # 总体标准差
    sstd = np.std(close_prices, ddof=1)     # 样本标准差
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
#计算收盘价的标准差
m = np.mean(closing_prices)
dev = closing_prices-m
var = np.mean(dev**2)
std = np.sqrt(var)
print(std)
std = np.std(closing_prices,ddof=1)
print(std)




