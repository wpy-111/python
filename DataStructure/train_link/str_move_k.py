"""
        字符串循环左移k位
            1.利用字符串的切片：切除前k位
            2.利用字符串相加，拼接
"""
class Solution:
    def string_left_k(self,string,k):
        left = string[:k]
        right = string[k:]
        return right+left


if __name__ == '__main__':
    s = Solution()
    string = 'abcXYZdef'
    print(s.string_left_k(string,3))

