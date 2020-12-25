"""
   练习
   古代的称，一斤是16两
   在终端中获取两，计算几斤几辆
 """


def input_price(price):
    jin = price // 16
    liang = price % 16
    return (jin,liang)
re = input_price(56)
print(re)
