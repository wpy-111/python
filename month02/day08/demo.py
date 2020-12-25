"""
   start调用run
"""
class A():
    def start(self):
        """ 复杂操作"""
        self.run()
    def run(self):
        pass
class B(A):
    def run(self):
        print('135')
b = B().start()
