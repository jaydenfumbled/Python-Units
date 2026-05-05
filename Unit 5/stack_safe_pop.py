class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def safe_pop(self):
        if not self.stack:
            print("Stack is empty, nothing to pop.")
            return None
        return self.stack.pop()


s = Stack()
s.push(10)
s.push(20)
print(s.safe_pop())
print(s.safe_pop())
print(s.safe_pop())
