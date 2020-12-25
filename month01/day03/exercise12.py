#猜数字
#程序产生1-100之间的随机数,让用户不不断猜测,直到猜对

import random
number = random.randint(1,100)
count = 1
while count <= 5:
    number01 = int(input("请输入数字"))
    count+=1
    if number01 < number:
          print("小了")
    elif number01 > number:
          print("大了")
    else:
           print("恭喜你答对了,总共猜了"+str(count)+"次")
           break
else:
    print("笨死")






