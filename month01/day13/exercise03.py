"""
   创建父类
        车（品牌，价格）
    创建子类
        电动车（充电容量，充电速度）
"""
class Car:
    def __init__(self, brand="", price=0):
        self.brand=brand
        self.price=price
class Scooter(Car):

    def __init__(self,brand,price,charging_capacity=0, charging_speed=0):
        super().__init__(brand,price)
        self.charging_capacity=charging_capacity
        self.charging_speed=charging_speed
s01=Scooter("小鸟",1000,750,10)