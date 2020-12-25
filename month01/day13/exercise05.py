"""
   随意重写两个算数运算符
"""
class Vector01:
    def __init__(self, x=0):
        self.x=x
    def __str__(self):
        return "结果是:%s"%(self.x)
    def __sub__(self, other):
        return Vector01(self.x-other.x)
    def __iadd__(self, other):
        self.x+=other.x
        return self
    def __imul__(self, other):
        self.x *= other.x
        return self
v01=Vector01(10)
v02=Vector01(50)
    # re=v01.__sub__(v02)
print(v01-v02)
v01+=v02
print(v01)
print(v02)
v01*=v02
print(v01)