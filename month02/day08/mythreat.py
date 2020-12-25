"""
   自定义线程类
"""
from threading import Thread
from time import ctime,sleep
# class MyThread(Thread):
#     def __init__(self, sec, song=""):
#         self.sec = sec
#         self.song = song
#         super().__init__()
#     def run(self):
#         self.player()
#     def player(self):
#         for i in range(3):
#             print("Playing %s %s"%(self.song,ctime()))
#             sleep(self.sec)
def player(sec,song):
    for i in range(3):
        print("Playing %s %s" % (song, ctime()))
        sleep(sec)
class MyThread(Thread):
    def __init__(self,target=None,args=(),kewards={}):
        super().__init__()
        self.target = target
        self.args = args
        self.kewards = kewards
    def run(self):
        self.target(*self.args,**self.kewards)

c = MyThread(target=player,args=(3,),kewards={'song':'凉凉'})
c.start()
c.join()
