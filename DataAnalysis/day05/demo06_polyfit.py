"""
    多项式拟合
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
datas,bhp_closing_prices = np.loadtxt('bhp.csv',delimiter=',',usecols=(1,6),
           dtype=('M8[D],f8'),unpack=True,converters={1:dmy2ymd})
vale_closing_prices = np.loadtxt('vale.csv',delimiter=',',usecols=(6),
           dtype=('f8'),unpack=True)
mp.figure('PolyFit',facecolor='lightgrey')
mp.title('PolyFit',fontsize=16)
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
#计算了两只股票的差价函数 做多项式拟合
diff_pries = bhp_closing_prices - vale_closing_prices
mp.plot(datas,diff_pries,color = 'dodgerblue',label='differ price')
days = dates.astype('M8[D]').astype('i4')
P = np.polyfit(days,diff_pries,4)
print(P)
y = np.polyval(P,days)
mp.plot(days,y,color='orangered',label='polyline')
mp.legend()
mp.tight_layout()
mp.gcf().autofmt_xdate()
mp.show()