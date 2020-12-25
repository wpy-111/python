thinkness =0.00001
count = 0
while thinkness <= 8844.43:
    thinkness *=2
    count += 1
    print("第" + str(count) + "次" + "对折的高度是" + str(thinkness) + "m")
