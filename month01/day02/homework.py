# 练习在终端中录入小时数,分钟数，秒数，计算总共的秒数
hour = float(input("请输入小时数:"))
minute = float(input("请输入分钟数"))
second = float(input("请输入秒钟数"))
result = hour*60*60
result +=minute*60
result += second
print("结果是："+str(result))