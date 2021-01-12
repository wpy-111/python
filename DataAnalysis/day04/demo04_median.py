"""
    中位数
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
#绘制收盘价格折线图，观察走势
mp.figure('AAPL',facecolor='lightgrey')
mp.title('AAPL',fontsize=16)
mp.xlabel("Data",fontsize=14)
mp.ylabel("Closing Prices",fontsize=14)
mp.grid(linestyle=':')
#修改x轴的刻度定位器
ax = mp.gca()
import matplotlib.dates as md
ax.xaxis.set_major_locator(md.WeekdayLocator(byweekday=md.MO))
ax.xaxis.set_major_formatter(md.DateFormatter("%d %m %Y"))  # %b表示月份简写
ax.xaxis.set_minor_locator(md.DayLocator())
#将dates转化为matplotlib内置的日期类型
dates = datas.astype(md.datetime.datetime)
mp.plot(datas,closing_prices,color='dodgerblue',linestyle='--',linewidth=2,
        alpha=0.8,label='closing prices')
#绘制均值平均线
m = np.mean(closing_prices)
mp.hlines(m,datas[0],datas[-1],color='red',label='Mean()')
#VMAP交易量加权平均价格
vmap = np.average(closing_prices,weights=volumes)
mp.hlines(vmap,datas[0],datas[-1],color='green',label='VMAP')
#TWAP 时间加权平均价格
times = np.linspace(1,3,closing_prices.size)
tmap = np.average(closing_prices,weights=times)
mp.hlines(tmap,datas[0],datas[-1],color='dodgerblue',label='TMAP')
#中位数
median = np.median(closing_prices)
mp.hlines(median,datas[0],datas[-1],color='pink',label='Median')
mp.legend()
#排序
sorted_prices = np.sort(closing_prices)
print(sorted_prices)
mp.tight_layout()
mp.gcf().autofmt_xdate()
mp.show()




