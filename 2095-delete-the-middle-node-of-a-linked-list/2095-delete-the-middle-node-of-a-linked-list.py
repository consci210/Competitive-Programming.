# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next :
            return None  
        
        slow , fast = head , head.next
        prev = None 
        while fast and fast.next :
            prev = slow
            slow = slow.next
            fast = fast.next.next 
        
        if not fast :
            prev.next = slow.next 
        elif not fast.next :
            slow.next = slow.next.next
            
        return head 