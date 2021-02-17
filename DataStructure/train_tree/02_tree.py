"""
    二叉树
"""
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def add(self,value):
        """添加节点"""
        node = Node(value)
        #空树情况
        if self.root == None:
            self.root = node
            return
        q = [self.root]
        while q:
            cur_node = q.pop(0)
            #判断左孩子
            if cur_node.left is None:
                cur_node.left = node
                return
            else:
                q.append(cur_node.left)
            #判断右孩子
            if cur_node.right is None:
                cur_node.right = node
                return
            else:
                q.append(cur_node.right)

    def breadth_travel(self):
        """广度遍历"""
        if self.root is None:
            return

        #非空树情况
        q = [self.root]
        while q:
            cur_node = q.pop(0)
            print(cur_node.value)
            if cur_node.left is not None:
                q.append(cur_node.left)
            if cur_node.right is not None:
                q.append(cur_node.right)

    def pre_travle(self):
        """深度遍历-根左右前序遍历"""





















