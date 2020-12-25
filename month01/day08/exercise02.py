# 作业：（扩展）根据图中算法，对方阵进行转置（用函数）
def transpose(list_materi):
    for c in range(0, len(list_materi) - 1):
        for i in range(c+1, len(list_materi)):
            list_materi[i][c], list_materi[c][i] = list_materi[c][i], list_materi[i][c]

list_result=[[1, 2, 3, 4, "a"],
             [5,6,7,8,"b"],
             [9,10,11,12,"c"],
             [13,14,15,16,"d"],
             [17,18,19,20,"e"]
             ]
transpose(list_result)
print(list_result)