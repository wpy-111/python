"""
  写出判断一个字符串是否是回文 的算法
"""

while True:
    world = input("请输入字符串:")
    if world == world[::-1]:
        print("属于回文")
        break

    else:
        print("不属于回文")