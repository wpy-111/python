"""
   练习:
       根据月日,计算这一年打第几天
"""

typle =(31,28,31,30,31,30,31,31,30,31,30,31)
# day01=0
while True:
    month=int(input("请输入月"))
    day = int(input("请输入日"))
#     for i in range(month-1):
#         day01 +=typle[i]
#     all=day01+day03
#     print(all)
    total_day= sum(typle[:month-1])
    sum_day =total_day+day
    print(sum_day)