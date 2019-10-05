"""
哈希表，采用链接法解决哈希冲突
- 构造迭代器，首先实现两个接口
    __next__ ：得到下一个元素；
    __iter__ ：返还迭代器
- 可以在同一个类中实现这两个接口，在__iter__中返回self，即自身这个迭代器
- 也可以在__iter__中返回一个其他的迭代器
- 调用其他类的函数时，要将类实例化
"""


class LinkList:
    class Node:
        def __init__(self, item=None):
            self.item = item
            self.next = None

    class LinkListIterator:  # 迭代器类
        def __init__(self, node):
            self.node = node

        def __next__(self):
            if self.node:
                cur_node = self.node
                self.node = cur_node.next
                return cur_node.item
            else:
                raise StopIteration

        def __iter__(self):
            return self

    def __init__(self, iterable=None):
        self.head = None
        self.tail = None
        if iterable:
            self.extend(iterable)

    def append(self, obj):  # 尾插
        s = LinkList.Node(obj)
        if not self.head:  # 判定是否为空
            self.head = s
            self.tail = s
        else:
            self.tail.next = s
            self.tail = s  # 更新尾指针

    def extend(self, iterable):
        for obj in iterable:
            self.append(obj)

    def find(self, obj):
        for n in self:
            if n == obj:
                return True
        else:
            return False

    def __iter__(self):
        return self.LinkListIterator(self.head)

    def __repr__(self):
        return "<<"+", ".join(map(str, self))+">>"  # map对self的每个元素转换成str


# 类似集合的结构
class HashTable:
    def __init__(self, size=101):
        self.size = size
        self.T = [LinkList() for _ in range(self.size)]  # 每个位置都是个空链表
                  # 调用其他类的函数的时候要把类实例化

    def h(self, k):
        return k % self.size

    def inster(self, k):
        i = self.h(k)
        if self.find(k):
            print("Duplicated Insert")
        else:
            self.T[i].append(k)

    def find(self, k):
        i = self.h(k)
        return self.T[i].find(k)


lk = LinkList([1, 2, 3, 4])
print(lk)
print(lk.find(2))
ht = HashTable()
ht.inster(0)
ht.inster(1)
ht.inster(3)
ht.inster(102)
ht.inster(508)
print(",".join(map(str, ht.T)))
