dict_commodity_info = {
    101: {"name": "屠龙刀", "price": 10000},
    102: {"name": "倚天剑", "price": 10000},
    103: {"name": "九阴白骨爪", "price": 8000},
    104: {"name": "九阳神功", "price": 9000},
    105: {"name": "降龙十八掌", "price": 8000},
    106: {"name": "乾坤大挪移", "price": 10000}
}
list_order = []
def shopping():
    """
        购物
    """
    while True:
        item = input("1键购买，2键结算。")
        if item == "1":
            buying()
        elif item == "2":
            settlement()

def settlement():
    print_order_info()
    totall_price = calculation_price()
    paying(totall_price)

def paying(totall_price):
    while True:
        money = float(input("总价%d元，请输入金额：" % totall_price))
        if money >= totall_price:
            print("购买成功，找回：%d元。" % (money - totall_price))
            list_order.clear()
            break
        else:
            print("金额不足.")

def calculation_price():
    totall_price = 0
    for item in list_order:
        commodity = dict_commodity_info[item["cid"]]
        totall_price += commodity["price"] * item["count"]
    return totall_price

def buying():
    shopping_info()
    order = create_order()
    list_order.append(order)
    print("添加到购物车。")

def create_order():

    while True:
        cid = int(input("请输入商品编号："))
        if cid in dict_commodity_info:
            break
        else:
            print("该商品不存在")
    count = int(input("请输入购买数量："))
    order = {"cid": cid, "count": count}
    return order

def shopping_info():
    for key, value in dict_commodity_info.items():
        print("编号：%d，名称：%s，单价：%d。" % (key, value["name"], value["price"]))

def print_order_info():
    for item in list_order:
        commodity = dict_commodity_info[item["cid"]]
        print("商品：%s，单价：%d,数量:%d." % (commodity["name"], commodity["price"], item["count"]))


shopping()
