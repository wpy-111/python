# 在终端中录入一个数字,作为边长,打印矩形
number=int(input("请输入一个数字:"))
print("*"*number)
for message in range((number-2)):
    print("*"+" "*(number-2)+"*")
print("*"*number)





