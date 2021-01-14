"""
    线性预测
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
mp.plot(datas,closing_prices,color='dodgerblue',linestyle='--',linewidth=2,
        alpha=0.8,label='closing prices')
#基于线性预测理论 预测股票价格
N = 4
pre_prices = np.zeros(closing_prices.size-2*N)
for j in range(pre_prices.size):
    A = np.zeros((N,N))
    for i in range(N):
        A[i,::] = closing_prices[j+i:i+j+N]
    B = closing_prices[j+N:j+N*2]
    #基于最小二乘法求系数
    x = np.linalg.lstsq(A,B)[0]
    pre_prices[j] = x.dot(B)#点乘 x[x1,x2,x3]   b[b1,b2,b3]     x.dot = x1*b1 + x2*b2 + x3*b3
mp.plot(datas[N*2:],pre_prices,'o-',color = 'orangered',label="pre_price")

mp.legend()
mp.tight_layout()
mp.gcf().autofmt_xdate()
mp.show()




