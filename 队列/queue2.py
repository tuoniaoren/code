"""
collections中实现了python的一些数据结构，deque为双向队列
"""
from collections import deque

q = deque()
q.append(1)  # append是队尾进入元素，即右进
print(q.popleft())
"""
默认的pop是队尾出元素，即右出。所以 popleft 即左出元素。 所以 append+popleft构成队列
appendleft+pop 即队首进，队尾出
"""
q = deque([1, 2, 3], 5)
"""
deque([1,2,3]) 相当于初始化一个队列，然后[1,2,3]依次进队
5：为队列的长度
当push的元素个数大于长度时，会将前面的元素覆盖。即若push 6个元素，则队首此时为2，1就被覆盖了。
"""
h = deque([1,2,3,4,5], 5)
h.append(6)
print(h.popleft())

"""
利用这个特性，可以用deque去实现一下Linux中的tail命令。
tail命令：返还文件中的后几项
"""


def tail(n):
    with open('test.txt', 'r') as f:
        q = deque(f, n)
        return q


for line in tail(5):
    print(line, end='')
