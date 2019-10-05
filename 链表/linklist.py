"""
单向链表的每个节点包含两个部分， 数据域item和指向下一个节点的指针next
"""


class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


a = Node(1)
b = Node(2)
c = Node(3)
a.next = b
b.next = c
print(a.next.item)


"""
链表的创建和遍历
- 头插法
- 尾插法
"""


def create_linklist_head(li):
    head = Node(li[0])  # 头结点
    for element in li[1:]:
        node = Node(element)
        node.next = head
        head = node
    return head  # 返回头结点


def create_linklist_tail(li):
    head = Node(li[0])
    tail = head
    for element in li[1:]:
        node = Node(element)
        tail.next = node
        tail = node
    return head


def print_linklist(lk):  # 遍历链表
    while lk:
        print(lk.item, end=",")
        lk = lk.next


lk1 = create_linklist_head([1, 2, 3])
lk2 = create_linklist_tail([1, 2, 3])
print_linklist(lk1)
print('\n')
print_linklist(lk2)
