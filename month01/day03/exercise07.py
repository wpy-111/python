# 在终端中录入一个整数，如果奇数为变量state
# 赋值为奇数字,否则赋值为偶数
number = int(input("输入一个整数:"))
state = "奇数" if number % 2 else "偶数"
print(state)
