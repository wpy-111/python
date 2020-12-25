"""
   练习:
   """
list_result=[
           [1,2,3,4],
           [5,6,7,8,],
           [9,10,11,12],
           [13,14,15,16]
        ]

# 1.打印二维列表第三行数据(一行一个)
for item in (list_result[2]):
    print(item)
# 2.打印二维列表第二列数据(一行一个)
for i in list_result:
    print(i[1])
# for i in range(4):
#     print(list01[i][1])
# 3.打印二维列表所有数据(表格状)
for r in list_result:
    for c in r:
        print(c,end="\t")
    print()
# 4.打印从下到上打印第三列数据(一行一个)
for m in range(3,-1,-1):
    print(list_result[m][2])
# 5.从右到左打印第四行数据(一行一个)
for x in range(3,-1,-1):
    print(list_result[3][x])