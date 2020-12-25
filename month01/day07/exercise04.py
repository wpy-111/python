"""
    矩阵转置
"""
list_result=[
           [1,2,3,4],
           [5,6,7,8,],
           [9,10,11,12],
           [13,14,15,16]
]
def transpose(list_line):
    list02=[]
    for c in range(4):
        line=[]
        for i in range(4):
            line.append(list_line[i][c])
        list02.append(line)
    return list02
re=transpose(list_result)
print(re)

# for i in range(4):
#     list0202.append(list01[i][1])
# list02.append(list0202)
# for i in range(4):
#     list0203.append(list01[i][2])
# list02.append(list0203)
# for i in range(4):
#     list0204.append(list01[i][3])
# list02.append(list0204)
# print(list02)
