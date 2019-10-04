class Queue:
    def __init__(self, size=100):
        self.queue = [0 for _ in range(size)]
        self.size = size
        self.rear = 0  # 队尾， 出队
        self.front = 0  # 队首，进队

    def push(self, element):
        if not self.is_full():
            self.queue[self.rear] = element
            self.rear = (self.rear + 1) % self.size
        else:
            raise IndexError("Queue is filled!")

    def pop(self):
        if not self.is_empty():
            new_data = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return new_data
        else:
            raise IndexError("Queue is empty!")

    def is_empty(self):
        return self.rear == self.front

    def is_full(self):
        return (self.rear + 1) % self.size == self.front


q = Queue(5)  # 长度为5的队列只能存放4个数
for i in range(4):
    q.push(i)
print(q.pop())
q.push(5)
print(q.pop())