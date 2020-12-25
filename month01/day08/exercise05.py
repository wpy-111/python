"""
   练习：
"""
def fun01(*args,**kwargs):
    print(args)
    print(kwargs)
fun01(2,5,84,"悟空",p="无数",m=85)




def fun02(a=15,b=75,*args,c=0,d=0,**kwargs):
    print(a)
    print(b)
    print(args)
    print(c)
    print(d)
    print(kwargs)
fun02(85,65,c=35,d=85,p=85,m=98)