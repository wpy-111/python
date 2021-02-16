"""
    反转单词split（）进行切割
          reverse（）反转列表
          join（） 列表拼接
"""
class Solution:
    def reverse_word(self,word):
        li = word.split()
        li.reverse()
        return  ' '.join(li)
if __name__ == '__main__':
    s = Solution()
    string = 'student a am I'
    print(s.reverse_word(string))