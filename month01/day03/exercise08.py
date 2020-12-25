# 在终端录入一个年份,如果是润年为变量day
# 赋值为29,否则为28
year = int(input("请输入年份:"))
day = 29 if not year % 400 or not year % 4 and year % 100 else 28
print(day)
