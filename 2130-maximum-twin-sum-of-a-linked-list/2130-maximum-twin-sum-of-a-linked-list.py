# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head.next.next :
            return (head.val + head.next.val)
        
        current = head
        slow , fast = head , head.next 
        largest_sum = 0
        while fast and fast.next :
            slow = slow.next 
            fast = fast.next.next
            
        middle_node = slow.next
        slow.next = None 
        
        prev = None 
        current = middle_node
        while current :
            next_node = current.next 
            current.next = prev
            prev = current 
            current = next_node 
        
        right_start = prev
        left_start = head 
        
        while right_start and left_start :
            current_sum = right_start.val + left_start.val 
            largest_sum = max(largest_sum , current_sum)
            right_start = right_start.next
            left_start = left_start.next
        
        return largest_sum 
