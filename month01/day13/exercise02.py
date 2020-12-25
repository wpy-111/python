"""
    行为上的继承
    定义父类
        动物：吃
    定义子类
        狗：跑
        鸟：飞
"""
class Animal:
    def eat(self):
        print("吃")
class Dog(Animal):
    def run(self):
        print("跑")
class Bird(Animal):
    def fly(self):
        print("飞")
