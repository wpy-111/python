"""
    感知机实现逻辑
"""
#实现逻辑和
def AND(x1,x2):
    w1,w2,theta = 0.5,0.5,0.7
    tmp = x1 * w1 + x2 * w2 
    if tmp <= theta:
        return 0
    else:
        return 1
#实现逻辑或
def OR(x1,x2):
    w1,w2,theta = 0.5,0.5,0.2
    tmp = x1 * w1 + x2 * w2 
    if tmp <= theta:
        return 0
    else:
        return 1
print(AND(int(input('x1:')),int(input('x2:'))))
print(OR(0,0))