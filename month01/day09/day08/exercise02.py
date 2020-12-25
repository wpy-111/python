"""
   练习2：定义函数，判断二维列表是否存在某个数字
   输入：二维列表，2
   输出：TRUE
"""
map = [       [2, 2, 0, 4],
              [0, 4, 8, 8 ],
              [2, 2, 2, 2 ],
              [0, 2, 2, 0]]
def judge_exist(list,number):
    for i in list:
        if number in i:
            return "true"
    return "false"
print(judge_exist(map,5))
