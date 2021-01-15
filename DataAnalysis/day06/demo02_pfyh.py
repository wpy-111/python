"""
    浦发银行
"""
# import  numpy as np
# import matplotlib.pyplot as mp
#
# dates,opening_prices,highest_prices,lowest_price,closing_prices,ma5,ma10 \
#     = np.loadtxt('./pfyh.csv',delimiter=',',usecols=(0,1,2,3,4,5,6),unpack=True,dtype='M8[D],f8,f8,f8,f8,f8,f8')
# def profit(cdate):
#     # 设计一种投资策略,根据单钱时间，依据 均线理论，返回1(建议买入)0(观望)-1(卖出)
#     mdates = dates[dates<=cdate]
#     mm5 = ma5[dates<=cdate]
#     mm10 = ma10[dates<=cdate]
#     if mdates.size >=2:
#         if (mm5[-2] < mm10[-2]) & (mm5[-1] > mm10[-1]):#金叉
#             return 1
#         elif (mm5[-2] > mm10[-2]) & (mm5[-1] < mm10[-1]):#死叉
#             return -1
#         else:
#             return 0
#     else:
#         return 0
# #测试投资策略
# profits_vec = np.vectorize(profit)
# print(profits_vec(dates))
# mp.plot(dates,closing_prices)
# mp.show()
import numpy as np
import matplotlib.pyplot as mp
import datetime as dt
import matplotlib.dates as md

# 日期格式转换函数: 将日月年转换为年月日格式
def dmy2ymd(dmy):
    dmy = str(dmy, encoding="utf-8")
    # 从指定字符串返回一个日期时间对象
    dat = dt.datetime.strptime(dmy, "%Y/%m/%d").date()
    tm = dat.strftime("%Y-%m-%d")  # 格式化
    return tm

dates, opening_prices, highest_prices, lowest_prices, closing_prices, ma5, ma10= \
    np.loadtxt("./pfyh.csv", #文件路径
               delimiter=",", #指定分隔符
               usecols=(0,1,2,3,4,5,6), #读取的列(下标从0开始)
               unpack=True, #拆分数据
               dtype="M8[D], f8, f8, f8, f8, f8, f8") #
mp.plot(dates, closing_prices)
mp.show()
# 定义一种投资策略，传入日期，基于均线理论返回是否应该按收盘价购买 1:应买入  0:应持有现状  -1:应卖出
def profit(m8date):
    mma5 = ma5[dates < m8date]
    mma10 = ma10[dates < m8date]
    # 至少两天数据才可以进行预测
    if mma5.size < 2:
        return 0
    # 出现金叉，则建议买入
    if (mma5[-2] <= mma10[-2]) and (mma5[-1] >= mma10[-1]):
        return 1
    # 出现死叉，则建议卖出
    if (mma5[-2] >= mma10[-2]) and (mma5[-1] <= mma10[-1]):
        return -1
    return 0

# 矢量化投资函数
vec_func = np.vectorize(profit)
# 使用适量换函数计算收益
profits = vec_func(dates)
print(profits)

# 定义资产
assets = 1000000
stocks = 0
payment_price = 0
status = 0
for index, profit in enumerate(profits):
    current_price = closing_prices[index]
    # 如果是买入并且赔了的状态，若已经跌出5%，则强制卖出
    if status == 1:
        payment_assets = payment_price * stocks
        current_assets = current_price * stocks
        if (payment_assets > current_assets) and ((payment_assets-current_assets) > payment_assets *0.05):
            payment_price = current_price
            assets = assets + stocks * payment_price
            stocks = 0
            status = -1
            print('止损：dates:{}, curr price:{:.2f}, assets:{:.2f}, stocks:{:d}'.format(dates[index], current_price, assets, stocks))
    if (profit == 1) and (status != 1): # 买入
        payment_price = current_price
        stocks = int(assets / payment_price)
        assets = assets - stocks * payment_price
        status = 1
        print('买入：dates:{}, curr price:{:.2f}, assets:{:.2f}, stocks:{:d}'.format(dates[index], current_price, assets, stocks))
    if (profit == -1) and (status != -1): # 卖出
        payment_price = current_price
        assets = assets + stocks * payment_price
        stocks = 0
        status = -1
        print('卖出：dates:{}, curr price:{:.2f}, assets:{:.2f}, stocks:{:d}'.format(dates[index], current_price, assets, stocks))
    # print('持有：dates:{}, curr price:{:.2f}, assets:{:.2f}, stocks:{:d}'.format(dates[index], current_price, assets, stocks))