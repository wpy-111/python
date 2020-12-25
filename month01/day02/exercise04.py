"""
   练习
   古代的称，一斤是16两
   在终端中获取两，计算几斤几辆
       35         2    3
"""
int_number = int(input("请输入两书："))
jin = int_number // 16
liang = int_number % 16
print(str(jin) + "斤" + str(liang) + "两")

