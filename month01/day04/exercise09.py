"""
   练习
   1.创建列表,存储"水星","金星","地球","木星","天王星",
   2.在列表中末尾追加"海王星",在地球后面插入"火星"
   3.打印距离太阳最近的行星
   4.打印距离太阳最远的行星
   5.打印距离到地球中间的所有行星(一行一个)
   6.将地球后面的所有行星删除
"""
list_result =["水星", "金星", "地球", "木星", "天王星"]
# print(list01)
list_result.append("海王星")
list_result.insert(3, "火星")
# print(list01)
# print(list01[0])
# print(list01[-1])
# for message in list01[:2]:
#     print(message)
# del list01[3:]
print(list_result[-3:-1:1])