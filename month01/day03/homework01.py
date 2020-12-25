#作业在终端中录入年份,显示季度

while True:
    month = int(input("输入月份:"))
    if month < 1or month >12:
        print("输入错误")
    elif month <=4:
        print("春天")
    elif month <=7:
        print("夏天")
    elif month <=10:
        print("秋天")
    elif month <=13:
        print("冬天")

