class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class LinkedListStack:
    def __init__(self):
        self.head = None
        self.size = 0
        self.max_value = float('-inf')  # 초기화가 필요합니다.
        self.max_key = None

    def is_empty(self):
        return self.head is None

    def get_max(self):
        return (self.max_key, self.max_value)

    def push(self, key, value):
        new_node = Node(key, value)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

        if value > self.max_value:
            self.max_value = value
            self.max_key = key

    def pop(self):
        if self.size == 0:
            return -1
        def get_next_node(node):
            return node.next
        
        pop_result = self.head

        # pop_result.key가 max_key와 같지 않은 경우
        if pop_result.key != self.max_key:
            self.head = pop_result.next
            self.size -= 1
            print("max",  self.max_key)
            return (pop_result.key, pop_result.value)

        # pop_result.key가 max_key와 같고 다음 노드가 존재할 경우
        if pop_result.next is not None and self.max_key == pop_result.key:
            self.max_value = pop_result.next.value
            self.max_key = pop_result.next.key
            temp_node = get_next_node(pop_result.next)

            while temp_node is not None:
                if temp_node.value > self.max_value:
                    self.max_value = temp_node.value
                    self.max_key = temp_node.key
                temp_node = get_next_node(temp_node)
                print("max",  self.max_key)

        # 헤드 이동 및 크기 감소는 함수 내에서 한번만!
        self.head = pop_result.next
        self.size -= 1
        return (pop_result.key, pop_result.value)

stack = LinkedListStack()
stack.push(1, 20)
stack.push(2, 20)
stack.push(3, 30)
print(stack.get_max())  # 예상 (2, 20)
print(stack.pop())
print(stack.get_max())  # 예상 (3, 15)
print(stack.pop())
print(stack.get_max())  # 예상 (1, 10)
print(stack.pop())
print(stack.pop())      # 빈 스택이므로 -1



