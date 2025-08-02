class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.is_empty():
            return -1
        else:
            return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

    def get_sum(self):
        return sum(self.stack)

    def size(self):
        return len(self.stack)


k = int(input())
stack = Stack()

for _ in range(k):
    a = int(input())
    if a == 0:
        stack.pop()
    else:
        stack.push(a)

print(stack.get_sum())
