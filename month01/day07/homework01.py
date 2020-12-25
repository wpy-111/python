"""
   作业：（扩展）根据图中算法，对方阵进行转置（不用函数）
"""
list_result=[
           [1,2,3,4,"a"],
           [5,6,7,8,"b"],
           [9,10,11,12,"c"],
           [13,14,15,16,"d"],
           [17,18,19,20,"e"]
        ]
# list[0][1]    list[1][0]
# list[0][2]    list[2][0]
# list[0][3]    list[3][0]

# for i in range(1,4):
# list[1][2]        list[2][1]
# list[1][3]        list[3][1]
# for c in range(2,4)
for c in range(0, len(list_result) - 1):
    for i in range(c+1, len(list_result)):
        list_result[i][c], list_result[c][i] = list_result[c][i], list_result[i][c]
print(list_result)

# for i in range(2,-1,-1):
#     for c in range(3,i,-1):
#         list01[i][c], list01[c][i]=list01[c][i],list01[i][c]
# print(list01)
