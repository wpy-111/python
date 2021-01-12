"""
      协方差
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
mp.figure('COV',facecolor='lightgrey')
mp.title('COV',fontsize=16)
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
#把bhp和vale两支股票
mp.plot(dates,bhp_closing_prices,linestyle='-',linewidth=2,alpha=0.8,color='dodgerblue',label='bhp')
mp.plot(dates,vale_closing_prices,linestyle='-',linewidth=2,alpha=0.8,color='orangered',label='vale')
#计算两组数据的协方差
m_bhp = np.mean(bhp_closing_prices)
m_vale = np.mean(vale_closing_prices)
dev_bhp = bhp_closing_prices - m_bhp
dev_vale = vale_closing_prices - m_vale
cov = np.mean(dev_bhp*dev_vale)
print(cov)
#计算两组数据的相关系数  coef
coef = cov / (np.std(bhp_closing_prices)*np.std(vale_closing_prices))
print(coef)
#获取两组数据统计相关系数的方法API:相关矩阵
coef = np.corrcoef(bhp_closing_prices,vale_closing_prices)
print(coef)
#np.cov()：协方差矩阵 对角线是方差
cov = np.cov(bhp_closing_prices,vale_closing_prices)
print(cov)
mp.legend()
mp.tight_layout()
mp.gcf().autofmt_xdate()
mp.show()