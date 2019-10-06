"""
tree模拟文件系统
"""


# 节点定义
class Node:
    def __init__(self, name, type='dir'):
        self.name = name
        self.type = type  # "dir" or "file"
        self.children = []  # 链式存储
        self.parent = None

    def __repr__(self):
        return self.name
"""
__repr__() 是一个非常特殊的方法，它是一个“自我描述”的方法，该方法通常用于实现这样一个功能：
当程序员直接打印该对象时，系统将会输出该对象的“自我描述”信息，用来告诉外界该对象具有的状态信息。
所以我们重写__repr__()函数从而得到返回自己想要的“自我描述”信息
n = Node("hello")
n2 = Node("world")
假设n2是n的子文件夹
n.children.append(n2)
n2.parent = n
"""


class FileSystemTree:
    def __init__(self):
        self.root = Node("/")
        self.now = self.root  # 当前自己所在目录

    def mkdir(self, name):  # 创建目录
        # name 以 / 结尾
        if name[-1] != "/":
            name += "/"
        node = Node(name)
        self.now.children.append(node)
        node.parent = self.now

    def ls(self):  # 显示当前目录的子目录
        return self.now.children

    def cd(self, name):
        if name[-1] != "/":
            name += "/"
        if name == "../":  # 返回父目录
            self.now = self.now.parent
            return
        for child in self.now.children:  # 切换到子目录
            if child.name == name:
                self.now = child
                return
        raise ValueError("invalid dir")

tree = FileSystemTree()
tree.mkdir("var/")
tree.mkdir("bin/")
tree.mkdir("usr/")
print(tree.ls())

tree.cd("bin/")
tree.mkdir("python/")
print(tree.ls())

tree.cd("../")
print(tree.ls())
