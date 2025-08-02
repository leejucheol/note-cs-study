class Queue:
	def __init__(self):
		self.queue = []

	def enqueue (self, value):
		self.queue.append(value)

	def dequeue (self):
		if not self.is_empty():
			return self.queue.pop(0)
		return None

	def size(self):
		return len(self.queue) 

	def is_empty(self):
		return len(self.queue) == 0
	
queue = Queue()
queue.enqueue("A")
queue.enqueue("B")
print(queue.dequeue())  # Should print "A"
print(queue.size())  # Should print 1