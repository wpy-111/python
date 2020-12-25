# 练习在终端中录入一个年份，打印天数
month = int(input("请输入几月"))
if month == 1 or month == 3 or month == 5 or month == 7 or month == 10 or month == 12:
    print("天数为三十一天")
elif month == 4 or month == 6 or month == 9 or month == 11:
    print("天数为三十天")
elif month == 2:
    print("天数为二十八")
else:
    print("月份有误")
