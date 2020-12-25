"""
   函数入门练习：******
               ******
               ******

"""
def print_shape(c_count,l_count,shape):
    """
      图形
    :param count: int 数量
    """
    for i in range(c_count,):
        for c in range(l_count):
            print(shape,end=" ")
        print()#换行
print_shape(5,10,"$")