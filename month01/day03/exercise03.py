# 练习  录入数字/运算符/数字
# 如果运算是+ - * / 打印结果，
number_one = float(input("请输入第一个数字："))
operate = input("请输入运算符：")
number_two = float(input("请输入第二个数字："))
if operate == "+":
    print(number_one + number_two)
elif operate == "-":
    print(number_one - number_two)
elif operate == "*":
    print(number_one * number_two)
elif operate == "/":
    print(number_one / number_two)
else:
    print("运算错误")
