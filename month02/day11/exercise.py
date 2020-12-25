"""
  输入端口，返回地址
"""
import re
# def main():
#     c = open('/home/tarena/桌面/exc.txt')
#     port = input("请输入端口：")
#     while True:
#         data = c.read(1024)
#         if data == port:
#             break
#     regx = re.compile(r'address is .+')
#     l = regx.findall(c.read())
#     print(l)
# main()
def get_address(port):
    f = open('/home/tarena/桌面/exc.txt')
    while True:
        data = ""
        for line in f:
            if line == "\n":
                break
            data +=line
        if not data:
            return "没有该端口"
        #获取首单词
        obj = re.match(r'\S+',data)
        if port ==obj.group():
            pattern = r"[0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4}"
            # pattern = r'address is \d+'
            obj = re.search(pattern,data)
            if obj:
                return  obj.group()
if __name__ == '__main__':
    print(get_address("BVI1"))
