"""
    2048游戏核心算法
"""
# 全局变量
# 1.定义函数，将0元素移动到末尾
def zero_to_end(list_merge):
    for i in list_merge[::-1]:
        if i == 0:
            list_merge.remove(i)
            list_merge.append(0)

list_merge = [4, 0, 4, 0]
zero_to_end(list_merge)
print(list_merge)

# 2.定义函数，合并相同的元素（非零）
def merge_element():
    zero_to_end(list_merge)
    for m in range(len(list_merge) - 1):
        if list_merge[m] == list_merge[m + 1]:
            list_merge[m] = list_merge[m] * 2
            del list_merge[m + 1]
            list_merge.append(0)
merge_element()
print(list_merge)
map = [       [2, 2, 0, 4],
              [0, 4, 8, 8 ],
              [2, 2, 2, 2 ],
              [0, 2, 2, 0]]

# # 3.向左移动一个
def move_left():
    global list_merge
    for line in map:
        list_merge = line
        merge_element()
move_left()
print(map)
# # 3.向右移动一个,并且合并元素
def move_right():
    global list_merge
    for line in map:
        list_merge=line[::-1]
        merge_element()
        line[::-1]=list_merge

move_right()
print(map)
#  向上移动一格
def transpose(list_merge):
    for c in range(0, len(list_merge)-1):
        for i in range(c+1,len(list_merge)):
            list_merge[i][c], list_merge[c][i] = list_merge[c][i], list_merge[i][c]

def move_up():
    transpose(map)
    move_left()
    transpose(map)
move_up()
print(map)
# 向下移动
def move_down():
    transpose(map)
    move_right()
    transpose(map)
move_down()
print(map)