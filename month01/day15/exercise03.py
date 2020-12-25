"""
   定义函数，根据年月日计算星期（星期几）
"""
import time
def calculate_weekdays(year,month,day):
    type_time=time.strptime("%d-%d-%d"%(year,month,day),"%Y-%m-%d")
    list=["星期一","星期二","星期三","星期四","星期五","星期六","星期日",]
    return     list[type_time[6]]
print(calculate_weekdays(2020,8,6))
# 定义函数  根据生日计算活了多少天
def all_day(year,month,day):
    type_time=time.strptime("%d-%d-%d"%(year,month,day),"%Y-%m-%d")
    born_time=time.mktime(type_time)
    now_time=time.time()
    live_time=now_time-born_time
    live_day=live_time//(3600*24)
    return live_day
print(all_day(2001,5,6))