# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow , fast = head , head
        if not head or not head.next :
            return True 
    
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None 
        current = slow 
        
        while current :
            next_node = current.next
            current.next = prev
            prev = current 
            current = next_node 
        
        start ,end = head , prev
        while end :
            if start.val != end.val :
                return False
            start = start.next 
            end = end.next 
        return True
