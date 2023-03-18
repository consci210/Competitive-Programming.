# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        current = head 
        dummy =ListNode()
        dummy.next = head 
        prev = dummy
        while current :
            next_node = current.next
            if current.val == val :
                prev.next = next_node
            else :
                prev = current 
            current = next_node
        return dummy.next