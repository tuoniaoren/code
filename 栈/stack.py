class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        return self.stack.pop()

    def get_top(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0


def brace_match(s):
    match = {'}': '{', ']': '[', ')': '('}
    stack = Stack()
    for ch in s:
        if ch in {'(', '[', '{'}:
            stack.push(ch)
        else:
            if stack.is_empty():
                return False
            elif stack.get_top() == match[ch]:  # 栈顶元素匹配
                stack.pop()
            else:  # 栈顶元素不匹配
                return False
    if stack.is_empty():  # 读完所有元素，如果栈不为空，则false
        return True
    else:
        return False


a = "()(){}[]"
b = "({}[}"
print(brace_match(a))
print('---------')
print(brace_match(b))
