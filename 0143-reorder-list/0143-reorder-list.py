# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow , fast = head , head
        while fast and fast.next :
            slow = slow.next
            fast = fast.next.next
            
        middle = slow.next
        slow.next = None 
        prev = None 
        
        while middle :
            next_node = middle.next
            middle.next = prev
            prev = middle 
            middle = next_node 
        
        start = head 
        
        while prev :
            start_next = start.next
            prev_next = prev.next 
            start.next = prev 
            prev.next = start_next
            start = start_next 
            prev = prev_next

            
      