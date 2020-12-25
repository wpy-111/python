# 怜惜在终端中了录入一个多位整数
# 计算每位数相加和
number = input("请输入一个多位整数:")
result = 0
for txt in number:
    result += int(txt)
print(result)



