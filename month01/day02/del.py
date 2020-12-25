# 练习
# 在终端中录入一个年份，判断是否为润年，打印Ture,False
# 条件：年份能被4整除，但是不能被100整除
#     年分能被400整除
year = int(input("年份："))
print(year % 2 == 0 and year % 100 != 0 or year % 400 == 0)
