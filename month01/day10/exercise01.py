"""
   练习:创建狗类
   数据：爱称，品种，价格
   行为：叫
   创建两个狗对象，分别调用狗打行为
   画出内存图
"""
class Dog:
    def __init__(self,call,varieties,price):
        self.call=call
        self.varieties=varieties
        self.price=price
    def cry(self):
        print(self.varieties,"旺旺叫",sep="-")
w01=Dog("皮卡丘","金毛",3000)
w02=Dog("二横子","二哈",1000)
w01.varieties = 'shazi'
w01.cry()
w02.cry()
