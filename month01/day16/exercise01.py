"""
   定义函数，获取成绩（0-100）
"""
def get_scores():
    while True:
        try:
            score=int(input("请输入成绩："))
            if 0<=score<=100:
                return score
            else:
                print("输入范围错误")
        except:
            print("输入的不是整数")
get_scores()

