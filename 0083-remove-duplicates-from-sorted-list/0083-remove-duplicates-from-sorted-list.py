# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head :
            return head 
        current = head
        seen = dict()
        prev = ListNode() 
        while current :
            next_node = current.next 
            if current.val in seen.values() :
                prev.next = next_node    
            else :
                seen[current] = current.val 
                prev = current 
            current = next_node 
        
        return head
