"""
    数据平滑
"""
import matplotlib.dates as md
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
mp.figure('Smooth',facecolor='lightgrey')
mp.title('Smooth',fontsize=16)
mp.xlabel("Data",fontsize=14)
mp.ylabel("Profits",fontsize=14)
mp.grid(linestyle=':')
#修改x轴的刻度定位器
ax = mp.gca()
ax.xaxis.set_major_locator(md.WeekdayLocator(byweekday=md.MO))
ax.xaxis.set_major_formatter(md.DateFormatter("%d %m %Y"))  # %b表示月份简写
ax.xaxis.set_minor_locator(md.DayLocator())
#将dates转化为matplotlib内置的日期类型
dates = datas.astype(md.datetime.datetime)
#绘制两只股票收益率曲线
bhp_profit = np.diff(bhp_closing_prices) / bhp_closing_prices[1:]
vale_profit = np.diff(vale_closing_prices) / vale_closing_prices[1:]
mp.plot(datas[1:],bhp_profit,color='dodgerblue',label='bhp profit',alpha=0.3,linestyle='--')
mp.plot(datas[1:],vale_profit,color='orangered',label='vale profit',alpha=0.3,linestyle='--')
#针对两只股票执行卷积降噪
datas = datas[1:]
#hanning数据对称
kernal = np.hanning(8)
kernal = kernal / kernal.sum()
bhp_convolved = np.convolve(bhp_profit,kernal,'valid')
vale_convolved = np.convolve(vale_profit,kernal,'valid')
mp.plot(datas[7:],bhp_convolved,color='dodgerblue',alpha=0.5,linestyle='-',label='bhp profit')
mp.plot(datas[7:],vale_convolved,color='orangered',alpha=0.5,linestyle='-',label='vale profit')
#进行拟合
days = datas[7:]
days = days.astype('M8[D]').astype('i4')
bhp_p = np.polyfit(days,bhp_convolved,3)
vale_p = np.polyfit(days,vale_convolved,3)
bhp_y = np.polyval(bhp_p,days)
vale_y = np.polyval(vale_p,days)
mp.plot(days,bhp_y,linestyle='-',linewidth=3,color='dodgerblue',label='bhp profit')
mp.plot(days,vale_y,linestyle='-',linewidth=3,color='orangered',label='vale profit')
#求两个多项式的焦点
poly_diff = np.polysub(bhp_p,vale_p)
xs = np.roots(poly_diff)
print(xs.astype('M8[D]'))
mp.legend()
mp.tight_layout()
mp.gcf().autofmt_xdate()
mp.show()