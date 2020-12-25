"""
   练习在终端中录入四个同学体重
   打印最沉的体重
   思路：
      假设第一个是最大的
      以此与后面的元素比较
      发现更大的，则更换假设
"""
# weight = float(input("第一个同学体制"))
# weight1 = float(input("第二个同学体制"))
# weight2 = float(input("第三个同学体制"))
# weight3 = float(input("第四个同学体制"))
# if weight > weight1 and weight2 and weight3:
#     print("第一个同体重最重")
# if weight1 > weight and weight2 and weight3:
#     print("第二个同体重最重")
# if weight2 > weight and weight2 and weight3:
#     print("第三个同体重最重")
# if weight3 > weight1 and weight2 and weight:
#     print("第四个同体重最重")
weight = float(input("第一个同学体制"))
weight1 = float(input("第二个同学体制"))
weight2 = float(input("第三个同学体制"))
weight3 = float(input("第四个同学体制"))
max_value = weight
if max_value < weight1:
    max_value = weight1
if max_value < weight2:
    max_value = weight2
if max_value < weight3:
    max_value = weight3
print(max_value)
