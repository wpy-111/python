"""
    替换字符串
    replace()
     参数：old:将被替换的字符串
          new：新字符串
          max：字符串替换次数不超过max
"""
str = 'we are family'
new_str = str.replace(' ','$20')
print(new_str)
class Solution:
    def replace_space_string(self,string):
        return string.replace(' ','%20')

if __name__ == '__main__':
    s = Solution()
    string = 'we are family'
    print(s.replace_space_string(string))
