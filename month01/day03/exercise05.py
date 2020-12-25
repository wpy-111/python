#练习  在终端录入一个成绩，打印成绩
#优秀   良好    及格   不及格  成绩错误
achement = float(input("成绩:"))
if 90 <= achement <=100:
    print("成绩优秀")
elif 80 <= achement < 90:
    print("成绩良好")
elif 60 <= achement <80:
    print("成绩合格")
elif 0<= achement < 60:
    print("成绩不合格")
else:
    print("成绩有误")


