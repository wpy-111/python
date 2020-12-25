"""
   分叉树
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    """二叉树类"""
    def __init__(self,node=None):
        self.root = node

    def add(self,value):
        """在树中添加一个结点"""
        node = Node(value)
