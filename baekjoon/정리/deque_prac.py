class Deque:
	def __init__(self):
		self.deque = []

	def add_front (self, value):
		self.deque.insert(0, value)

	def add_back (self, value):
		self.deque.append(value)

	def remove_front(self):
		if not self.is_empty():
			return self.deque.pop(0)
		return None

	def remove_rear(self):
		if not self.is_empty():
			return self.deque.pop()
		return None

	def size(self):
		return len(self.deque) 

	def is_empty(self):
		return len(self.deque) == 0
	
deque = Deque()
deque.add_front("A")	
deque.add_back("B")
print(deque.remove_front())  # Should print "A"