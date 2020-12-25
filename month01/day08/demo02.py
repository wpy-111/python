"""
   函数参数:
       形式参数
"""
def fun01(*,p2,p3=53):

    print(p2)
    print(p3)
    # print(p2)
    # print(p3)
# fun01()
fun01(p2=6)
def fun02(a,*,d=85,**kwargs):
    print(d)
    print(a)
    print(kwargs)
fun02(a=85,b=75,c=36)