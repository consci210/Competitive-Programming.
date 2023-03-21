# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        current = head 
        def reverse (current) :
            if current == None :
                return current 
            if current.next == None :
                return current 
            if current.next.next == None :
                next_node = current.next 
                next_node.next = current
                current.next = None 
                return next_node 
            
            next_node = current.next
            next_to_next = next_node.next
            next_node.next = current 
            current.next = reverse(next_to_next)
            return next_node 
        return reverse(head)
            
            