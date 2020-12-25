"""
   函数参数
       实际参数
"""
def fun01(p1,p2,p3):
    print(p1)
    print(p2)
    print(p3)
# fun01(1,2,4)
# list01={1,5,6}
# fun01(*list01)
# fun01(p2=1,p1=5,p3=9)
dict01={"p2":5,"p1":8,"p3":9}
fun01(**dict01)