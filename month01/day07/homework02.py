"""
   定义函数，将二维列表，以表格状打印在zhongduanzhong
"""
def print_form(list):
    for r in list:
        for c in r:
            print(c, end="\t")
        print()
print_form([
           [1,2,3,4],
           [5,6,7,8,],
           [9,10,11,12],
           [13,14,15,16]
            ] )