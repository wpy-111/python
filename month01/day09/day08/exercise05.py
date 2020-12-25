"""
   练习 ：
       杨辉三角
       输入：6
       输出：
              [
                      [1]
                     [1,1]
                    [1,2,1]
                   [1,3,3,1]
                  [1,4,6,4,1]
                [1,5,10,10,5,1]

"""
list=[]
def pascal_triangle(number):
    for i in range(0,number):
        list_line=[]
        if i ==0:
            list_line=[1]
            list.append(list_line)
        elif i==1:
            list_line=[1,1]
            list.append(list_line)
        else:
            list_line.append(1)
            for m in range(1,i) :
                list_line.append(list[i-1][m-1]+list[i-1][m])
            list_line.append(1)
            list.append(list_line)
pascal_triangle(12)
print(list)

