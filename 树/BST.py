"""
二叉搜索树
- 插入（初始化二叉搜索树）
- 查询
- 删除
"""

class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None  # 左孩子
        self.rchild = None  # 右孩子
        self.parent = None


class BST:
    def __init__(self, li=None):
        self.root = None
        if li:
            for val in li:
                self.insert_no_rec(val)

    def insert(self, node, val):  # val是插入的值，node是查询的结点
        if not node:
            node = BiTreeNode(val)
        elif val < node.data:
            node.lchild = self.insert(node.lchild, val)
            node.lchild.parent = node
        elif val > node.data:
            node.rchild = self.insert(node.rchild, val)
            node.rchild.parent = node
        return node

    def insert_no_rec(self, val):  # 非递归的插入
        p = self.root
        if not p:  # 空树
            self.root = BiTreeNode(val)
            return
        while True:
            if val < p.data:
                if p.lchild:  # 如果存在左子树，则转化到左子树
                    p = p.lchild
                else:  # 如果左子树为空，则直接插入即可
                    p.lchild = BiTreeNode(val)
                    p.lchild.parent = p
                    return
            elif val > p.data:
                if p.rchild:
                    p = p.rchild
                else:
                    p.rchild = BiTreeNode(val)
                    p.rchild.parent = p
                    return
            else:
                return

    def query(self, node, val):  # node就是为了其递归作用
        if not node:  # node为空，即找不到
            return None
        if node.data > val:
            return self.query(node.lchild, val)
        elif node.data < val:
            return self.query(node.rchild, val)
        else:
            return node

    def query_no_rec(self, val):  # 非递归查找
        p = self.root
        while p:
            if p.data < val:
                p = p.rchild
            elif p.data > val:
                p = p.lchild
            else:
                return p
        return None

    # 前序遍历
    def pre_order(self, root):
        if root:
            print(root.data, end=",")
            self.pre_order(root.lchild)
            self.pre_order(root.rchild)

    # 中序遍历
    def in_order(self, root):
        if root:
            self.in_order(root.lchild)
            print(root.data, end=",")
            self.in_order(root.rchild)

    # 后序遍历
    def post_order(self, root):
        if root:
            self.post_order(root.lchild)
            self.post_order(root.rchild)
            print(root.data, end=',')

    def __remove_node_1(self, node):
        # 情况1：node是叶子节点
        if not node.parent:  # 根节点
            self.root = None
        if node == node.parent.lchild:  # node是其父亲的左孩子
            node.parent.lchild = None
        else:  # node是其父亲的右孩子
            node.parent.rchild = None

    def __remove_node_21(self, node):
        # 情况2.1：node只有一个左孩子
        if not node.parent:  # 根节点
            self.root = node.lchild
            node.lchild.parent = None
        elif node == node.parent.lchild:  # node是其父亲的左孩子
            node.parent.lchild = node.lchild
            node.lchild.parent = node.parent
        else:
            node.parent.rchild = node.lchild
            node.lchild.parent = node.parent

    def __remove_node_22(self, node):
        # 情况2.2：node只有一个右孩子
        if not node.parent:
            self.root = node.rchild
        elif node == node.parent.lchild:
            node.parent.lchild = node.rchild
            node.rchild.parent = node.parent
        else:
            node.parent.rchild = node.rchild
            node.rchild.parent = node.parent

    def delete(self, val):
        if self.root:  # 不是空树
            node = self.query_no_rec(val)  # 查找到该node
            if not node:  # node不存在
                return False
            if not node.lchild and not node.rchild:  # 叶子节点
                self.__remove_node_1(node)
            elif not node.rchild:  # 只有一个左孩子
                self.__remove_node_21(node)
            elif not node.lchild:  # 只有一个右孩子
                self.__remove_node_22(node)
            else:  # 情况3，两个孩子都有
                min_node = node.rchild
                while min_node.lchild:  # 查找后继节点
                    min_node = min_node.lchild
                node.data = min_node.data
                # 删除min_mode
                if min_node.rchild:  # 后继节点又可以分成叶子节点和有右孩子这两个情况
                    self.__remove_node_22(min_node)  # 有右孩子
                else:
                    self.__remove_node_1(min_node)  # 叶子节点

li = list(range(0, 100, 2))
import random
random.shuffle(li)
tree = BST(li)
tree.pre_order(tree.root)
print("")
tree.in_order(tree.root)
print("")
tree.post_order(tree.root)
print("")
print(tree.query_no_rec(4).data)
print(tree.query_no_rec(3))

tree1 = BST([1, 4, 2, 5, 3, 8, 6, 9, 7])
tree1.in_order(tree1.root)
print("")
tree1.delete(4)
tree1.delete(7)
tree1.in_order(tree1.root)
