"""
   随机加法考试题
   产生两个随机数
   在终端录入结果,提示:5+4=?
   答对+10,否则-5
   总共三道题,最后显示总分
"""
score=0
for message in range(3):
    import random
    random_number01= random.randint(1,10)
    random_number02= random.randint(1,10)
    input_result=int(input(str(random_number01)+ "+" +str(random_number02)+"="))
    if input_result == random_number01+random_number02:
        score += 10
    else:
        score -= 5
print(str(score))

