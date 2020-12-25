"""
   练习在终端录入一个四位数字：5203
   计算每位相加和5+2+0+3>10
"""
number = int(input("请输入四位数字："))
number01 = number % 10
number02 = (number // 10) % 10
number03 = (number // 100) % 10
number04 = number // 1000
result = number01 + number02 + number03 + number04
print("结果是:" + str(result))
