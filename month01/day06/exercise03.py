"""
   根据季度,打印月份
"""
dict={"春天":"1月2月3月",
      "夏天":"4月5月6月",
      "秋天":"7月8月9月",
      "冬天":"10月11月12月"
      }

seaon=input("请输入季节:")
if seaon in dict:
    print(dict[seaon])
else:
    print("输入有误")
