"""
   将下列代码定义到函数中，根据季度获取月份gongneng
"""
def date(seaon):
    if seaon == "春天":
        return ("1月，2月，3月")
    if seaon == "夏天":
        return ("4月，5月，6月")
    if seaon == "秋天":
        return ("7月，8月，9月")
    if seaon == "冬天":
        return ("10月，11月，12月")
print(date("夏天"))
