#练习  在终端录入一个成绩，打印成绩
#优秀   良好    及格   不及格  成绩错误
def evaluation(achement):
    if 90 <= achement <=100:
        return "成绩优秀"
    if 80 <= achement < 90:
        return "成绩良好"
    if 60 <= achement <80:
        return"成绩合格"
    if 0<= achement < 60:
        return "成绩不合格"
    return "成绩有误"
print(evaluation(100))
