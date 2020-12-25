"""
   水仙花数：各个数字立方和等于该数字的本身
   定义函数，根据位数计算水仙花数
   输入：3
   输出：[153,370,371,407]
"""
list = []


def calculate():
    for i in range(100, 1000):
        result = 0
        m = str(i)
        for x in m:
            result += int(x) ** 3
        if result == i:
            list.append(i)
calculate()
print(list)
