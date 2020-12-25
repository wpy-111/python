# 作业 BMI:用体重千克除以身高米的平方
# 小于18.5(不包含) 体重过低
# 18.5(不包含)------24(不包含) > 正常
# 24(不包含)------28(不包含) > 超重
# 28(不包含)------30(不包含) > 一度肥胖
# 30(不包含)------40(不包含) > 二度肥胖
# 大于等于40----重度肥胖
while True:
    weight = float(input("请输入体重(kg):"))
    long = float(input("请输入身高(m):"))
    BMI = weight / long ** 2
    if BMI < 18.5:
        print(str(BMI) + "体重过低")
    elif BMI < 24:
        print(str(BMI) + "体重正常")
    elif BMI < 28:
        print(str(BMI) + "超重")
    elif BMI < 30:
        print(str(BMI) + "一度肥胖")
    elif  BMI < 40:
        print(str(BMI) + "二度肥胖")
    else:
        print(str(BMI) + "重度肥胖")
