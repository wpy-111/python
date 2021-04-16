
x =  open('label.txt','a+')
with open('linelabellist.txt','r')as f:
    while True:
        line = f.readline()
        print(line)
        con = line.split(' ')
        print(con)
