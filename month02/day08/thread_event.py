"""
  互斥方法演示
"""
from threading import Event,Thread
s = None
e = Event()
def 陈子荣():
    print("陈子荣前来拜见")
    global s
    s ="天王盖地虎"
    e.set()
t = Thread(target=陈子荣)
t.start()
e.wait()
print("说对口令就是自己人")
if s =="天王盖地虎":
    print("宝塔镇河妖")
    print("遇见对的人")
else:
    print("打死他.........")
t.join()
