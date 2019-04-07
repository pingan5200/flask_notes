class Stack(object):
    def __init__(self):
        self.data = []

    def push(self, val):
        self.data.append(val)

    def pop(self):
        return self.data.pop()


_stack = Stack()
_stack.push('a')
_stack.push('b')
# 后进先出  
print(_stack.pop())
print(_stack.pop())
