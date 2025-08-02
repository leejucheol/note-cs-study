class Stack:
	def __init__(self):
		self.stack = []

	def push (self, value):
		self.stack.append(value)

	def pop (self):
		if not self.is_empty():
			return self.stack.pop()
		return None

	def peek (self):
		if not self.is_empty():
			return self.stack[-1]
		return None


	def size(self):
		return len(self.stack) 

	def is_empty(self):
		return len(self.stack) == 0
	
stack = Stack()
stack.push("A")
stack.push("B") 
stack.is_empty()  # Should return False
print(stack.pop())  # Should print "B"
print(stack.peek())  # Should print "A"
print(stack.size())  # Should print 1
print(stack.is_empty())  # Should return False