"""
    布林图
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
datas,opening_prices,highest_prices,lowest_prices,closing_prices = \
    np.loadtxt('aapl.csv',delimiter=',',usecols=(1,3,4,5,6),
           dtype=('M8[D],f8,f8,f8,f8'),unpack=True,converters={1:dmy2ymd})
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
mp.plot(datas,closing_prices,color='dodgerblue',linestyle='-',linewidth=2,
        alpha=0.8,label='closing prices')

#自定义卷积核，基于加权卷积绘制五日均线
kernal = np.exp(np.linspace(-1,0,5))[::-1]
kernal = kernal / kernal.sum()
ma53 = np.convolve(closing_prices,kernal,'valid')
mp.plot(datas[4:],ma53,color='red',linewidth=3,alpha=0.4,label='MA-53')
#绘制上轨与下轨
stds = np.zeros(closing_prices.size-4)
for i in range(stds.size):
    stds[i] = closing_prices[i:i+5].std()
upper = ma53 + 2 * stds
lower = ma53 - 2 * stds
mp.plot(datas[4:],upper,color='green',label='upper')
mp.plot(datas[4:],lower,color='green',label='lower')
mp.fill_between(datas[4:],upper,lower,upper>lower,color='green',alpha=0.3)



mp.legend()
mp.tight_layout()
mp.gcf().autofmt_xdate()
mp.show()




