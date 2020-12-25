"""
   练习：收银台
   在终端录入一个商品单价 5
   在录入一个购买数量 3
   最后录入支付金额 20
   计算应该找回多少钱 5
"""
price = input("请输入商品单价：")
float_price = float(price)
count = input("请输入数量：")
int_count = int(count)
money = input("请输入支付金额：")
float_money = float(money)
result = float_money - float_price * int_count
print("找回金额："+str(result))
