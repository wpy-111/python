# 练习在终端中录入总秒数，计算几小时几分钟几秒
second = int(input("请输入总秒数:"))
result01 = second // 3600
result02 = (second % 3600) // 60
result03 = (second % 3600) % 60
print(str(result01) + "时" + str(result02) + "分" + str(result03) + "秒")
