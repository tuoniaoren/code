"""
二叉树
- 前序遍历
- 中序遍历
- 后序遍历
- 层次遍历
"""
from collections import deque


class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None  # 左孩子
        self.rchild = None  # 右孩子

    def __repr__(self):
        return self.data

a = BiTreeNode("A")
b = BiTreeNode("B")
c = BiTreeNode("C")
d = BiTreeNode("D")
e = BiTreeNode("E")
f = BiTreeNode("F")
g = BiTreeNode("G")

e.lchild = a
e.rchild = g
a.rchild = c
c.lchild = b
c.rchild = d
g.rchild = f

root = e


# 前序遍历
def pre_order(root):
    if root:
        print(root, end=",")
        pre_order(root.lchild)
        pre_order(root.rchild)
pre_order(root)
print('\n')


# 中序遍历
def in_order(root):
    if root:
        in_order(root.lchild)
        print(root, end=",")
        in_order(root.rchild)
in_order(root)
print('\n')


# 后序遍历
def post_order(root):
    if root:
        post_order(root.lchild)
        post_order(root.rchild)
        print(root, end=',')
post_order(root)
print('\n')


# 层次遍历，类似于广度优先,使用队列，父节点出队，左右孩子节点入队
def level_order(root):
    queue = deque()
    queue.append(root)
    while len(queue) > 0:  # 只要队列不空
        node = queue.popleft()
        print(node, end=',')
        if node.lchild:
            queue.append(node.lchild)
        if node.rchild:
            queue.append(node.rchild)
level_order(root)
