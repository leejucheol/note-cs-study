class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

class Linkedlist:

	def __init__ (self):
		self.head = None

	def append (self, value):
		new_node = Node(value)
		if self.head is None:
			self.head = new_node
			return
		s = self.head # 처음부터 시작
		while s.next:
			s = s.next # 탐색 마지막 노드까지 이동
		s.next = new_node # 마지막 노드에서 새로운 노드 추가

	def display (self):
		s = self.head
		while s:
			print(s.value, end='->')
			s = s.next
		print("none")

ll = Linkedlist()
ll.append("A")
ll.append("B")
ll.append("C")
ll.display()
