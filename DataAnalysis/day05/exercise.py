"""
    用户流失调查
"""
import numpy as np
import matplotlib.pyplot as mp

ID,type,extre_time,extre_flow,months,loss = \
    np.loadtxt('./CustomerSurvival.csv',delimiter=',',usecols=(0,1,2,3,8,9),unpack=True,
               dtype='i4,i4,f8,f8,i4,i4')
#统计额外时间 额外流量 使用月份三个字段最小值，最大值，平均值
max_time = np.max(extre_time)
min_flow = np.min(extre_flow)
mean_flow = np.mean(extre_flow)
print("额外时间最大值：",max_time)
print("额外流量最小值：",min_flow)
print("额外流量的均值：",mean_flow)
#统计所有额外的通话时长人数占总人数的比列，统计有额外流量人数占总人数的比例
mask01 = extre_time>0
mask02 = extre_flow>0
print("额外的通话时长人数占总人数的比列:",extre_time[mask01].size/extre_time.size)
print("有额外流量人数占总人数的比例:",extre_flow[mask02].size/extre_flow.size)
#统计把流量用超的人们平均套餐使用的月数
mask03 = extre_flow<0
print("流量用超的人们平均套餐使用的月数:",np.mean(months[mask03]))
#按列进行统计学指标分析（均值，最值，标准差）
def func(data):
    return data.mean(),data.std()
arry = np.column_stack((extre_time,extre_flow))
result = np.apply_along_axis(func,0,arry)
print(result)
#绘制散点图，观察额外剩余流量用户与用户是否流失之间的关系
# mp.figure('loss & flow',facecolor='lightgrey')
# mp.title('loss & flow',fontsize=16)
# mp.xlabel("flow",fontsize=14)
# mp.ylabel("loss",fontsize=14)
# mp.scatter(extre_flow,loss,c=loss,cmap='jet',s=35,marker='o',label='loss & flow')
#绘制所有非流失用户，绘制散点图，观察这些用户额外剩余流量（x）与额外剩余时间（y）之间的关系
# mp.figure('time & flow',facecolor='lightgrey')
# mp.title('time & flow',fontsize=16)
# mp.xlabel("flow",fontsize=14)
# mp.ylabel("time",fontsize=14)
# mask04 = loss==0
# mp.scatter(extre_flow[mask04],extre_time[mask04],s=50,label='time & flow',c=extre_flow[mask04],cmap='jet')
#使用数学模型拟合上一题的数据分布，尝试通过用户额外流量（x）来预测额外剩余通话时间
#
# A = np.column_stack((extre_flow,np.ones_like(extre_flow)))
# B = extre_time
# x = np.linalg.lstsq(A,B)[0]
# k,b = x[0],x[1]
# y = k*500+b
# print(y)
#基于概率分布规律预测
flow_m = np.mean(extre_flow)
flow_s = np.std(extre_flow)
time_m = np.mean(extre_time)
time_s = np.std(extre_time)
print(np.random.normal(flow_m,flow_s,10))
print(np.random.normal(time_m,time_s,10))
mp.grid(linestyle=':')
mp.legend()
mp.show()











