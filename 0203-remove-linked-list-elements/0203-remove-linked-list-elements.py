# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        # First loop
        while head and head.val == val:
            head = head.next

        current = head

        # Second loop
        while current:
            while current and current.next and current.next.val == val:
                current.next = current.next.next
            current = current.next
        return head