"""
    两个栈实现队列 完成队列的push和pop操作 队列中的元素为int类型
    思路：
        1.最终目标实现队列：先进先出fifo
        2.现有资源：两个栈（计划使用顺序表实现）
    设计：
        stack_A = [100,200,300] append(),pop()进行入栈和出栈
        stack_B = [] 也是用append(),pop()进行入栈和出栈
"""
class Solution:
    def __init__(self):
        #创建两个空栈
        self.stack_A = []
        self.stack_B = []

    def push(self,value):
        """入队操作：在stack_A中添加元素"""
        self.stack_A.append(value)

    def pop(self):
        """出队操作：在stack_B中弹出元素"""
        if self.stack_B:
            return self.stack_B.pop()

        while self.stack_A:
            self.stack_B.append(self.stack_A.pop())
        if self.stack_B:
            return self.stack_B.pop()
if __name__ == '__main__':
    s = Solution()
    s.push(100)
    s.push(200)
    s.push(300)
    print(s.stack_A)
    print(s.stack_B)
    print(s.pop())
    print(s.stack_A)
    print(s.stack_B)
    s.push(400)
    print(s.stack_A)
    print(s.stack_B)
    print(s.pop())