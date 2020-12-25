"""
   内置模块   time
"""
import time
#1.当前时间截（1970年1月1日起到现在经过的秒数）
print(time.time())
#2.时间元祖（年，月，日，时，分，秒，星期，年的天，夏令时的偏移量）
typle_time=time.localtime()
print(typle_time)
print(typle_time[1:6])
# 3. 时间截 ---->时间元祖
print(time.localtime(1596718710.2169883))
# 4. 时间元祖 ----> 时间截
print(time.mktime(typle_time))
# 5.时间元祖 ---->字符串
print(time.strftime("%Y年%m月%d日%H时%M分%S秒",typle_time))
# 6.字符串 ---->时间元祖
print(time.strptime("2020年5月6日10时5分6秒","%Y年%m月%d日%H时%M分%S秒"))
