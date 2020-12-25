"""
    缓冲机制
"""
f = open('txt','w',1)
while True:
    thing=input(">>")
    if not thing:
        break
    f.write(thing)
    #缓冲函数
    f.flush()
f.close()