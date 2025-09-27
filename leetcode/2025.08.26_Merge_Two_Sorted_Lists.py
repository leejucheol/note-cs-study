from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 리스트 두개를 일단 함치고 나서 sort -> sort함수를 사용해야해서 안됨
        # 리스트 각 노드를 크기 비교 
        temp = ListNode() # 맨 뒤에 있는 노드를 가르킴
        tail = temp

        while list1 and list2: # 두 리스트의 값이 존재할 경우

            # 각 주어진 리스트 값을 비교하여 list2가 클경우 tail다음은 list1이다. 
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

# 남은 노드들을 이어줌
        if list1:
            tail.next = list1
        else:
            tail.next = list2
        
        return temp.next

