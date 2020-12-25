"""
   字符串的函数
"""
name="清华   的 校训：持之 以 恒 . "
print(name.center(5,"-"))
# print(name.replace("清华","我的",1))
print(name.find("校训"))
print(name.isspace())#空白
print(name.count(" "))
name01=name.lstrip()#删除开头空白
print(name01)
name02=name.rstrip()#删除末尾空白
print(name02)
name03=name.strip()#删除开头和末尾空白
print(name03)
letter="我的sasfsdfasASADsaFDGAdfbi"
print(letter.lower())#将字符串变为小写
print(letter.upper())#将字符串变为大写
print(letter.swapcase())#将字符串小写变为大写，将大写变为小写