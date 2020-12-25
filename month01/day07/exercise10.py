# 怜惜在终端中了录入一个多位整数
# 计算每位数相加和
# 将下列代码，定义到函数中
def each_add(figuer):
    result = 0
    for txt in figuer:
        result += int(txt)
    return result
re = each_add("653")
print(re)
