# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next :
            return head 
        current = head
        first_even = None 
        count = 1
        while current and current.next :
            next_node = current.next
            if not first_even :
                first_even = next_node 
            current.next = current.next.next 
            count +=1
            prev = current 
            current = next_node 
        if count % 2 == 1  :
            current.next = first_even
        else : 
            prev.next = first_even 
        return head 