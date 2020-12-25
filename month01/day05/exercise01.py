"""
   在终端中录入所有同学的身高,如果录入空,
   则;
      倒序打印所有身高(一行一个)
      打印最高  max()
      打印最低   min()
      打印平均身高  sum()/len()
"""
txm=[]
while True :
    height = input("请输入身高:")
    if height == " ":
        break
    height = float(height)
    txm.append(height)
print(max(txm))
# for sad in txm[::-1]:
#     print(sad)