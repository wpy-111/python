# 累加10----50之间,个位不是2/5/9的数字
number = 0
for message in range(10,51):
    if message % 10 ==2 or message % 10 ==5 or message % 10 ==9:
        continue
    number += int(message)
print(number)