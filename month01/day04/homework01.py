"""
   一个小球从100米落下,
   每次弹回高度一半.
   请计算:
         总共弹起来多少次(最小弹起来的高度0.01m)
         整个过程经过多少米
"""
length = 100
itm = 100
count=0
while length/2 >=0.01:
    length=length /2
    itm += 2*length
    count+=1
else:
    print("总共弹起来%d次,整个过程经过%f米"%(count,itm))



