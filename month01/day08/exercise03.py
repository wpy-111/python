"""
   定义函数，根据时分秒计算总秒数
"""
def calculation_all_second(hour=0,minutes=0,second=0):
    return  hour*3600+minutes*60+second
re=calculation_all_second(2,60)
print(re)

