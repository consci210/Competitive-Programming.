# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        count = 1
        current = head
        prev = None
        while count < left:
            prev = current
            current = current.next
            count += 1 
        left_most = current 
        prev_node = prev
        
        while count <= right:
            next_node = current.next
            current.next = prev
            prev = current 
            current = next_node 
            count += 1
        
        left_most.next = current
        
        if prev_node:
            prev_node.next = prev
        else:
            head = prev
        
        return head
