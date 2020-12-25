"""
   扑克牌：
   "数字"：“A”,“2”,“3”,"4","5",”6","7","8","9","10","J","Q","K"
   "花色"："红桃","方片","梅花","黑桃"
"""
list_result=["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
list02=["红桃","方片","梅花","黑桃"]
list03=[]
for i in list02:
    for c in list_result:
        list03.append(i+c)
print(list03)
list03=[i + c for i in list02 for c in list_result]
print(list03)