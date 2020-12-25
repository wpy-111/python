"""
   定义函数fun01,统计被调用次数
"""
count=0
def fun01():
    global count
    count+=1
fun01()
fun01()
fun01()
fun01()
fun01()
fun01()
print(count)