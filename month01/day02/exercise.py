str_time = float(input("请输入时间:"))
str_initial = float(input("请输入初速度:"))
str_distance = float(input("请输入距离："))
result = 2 * (str_distance - str_time * str_initial) / str_time ** 2
print("结果是：" + str(result))
