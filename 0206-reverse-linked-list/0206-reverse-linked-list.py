# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None 
        current = head 
        if not current or not current.next :
            return current 
        
        while current :
            next_node = current.next
            
            if prev :
                current.next = prev 
                prev = current 
                
            else :
                prev = current 
                current.next = None 
            
            current = next_node 
            
        return prev 
            
            
            
            