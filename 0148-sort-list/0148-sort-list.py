# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def findMid(head):
            slow = head
            fast = head.next
            while fast and fast.next :
                slow = slow.next
                fast = fast.next.next
            return slow 
        
        def merge(left, right):
            dummy = ListNode()
            prev = dummy
            while left and right:
                if left.val < right.val:
                    prev.next = left 
                    left = left.next 
                else:
                    prev.next = right 
                    right = right.next 
                prev = prev.next 
            
            if left:
                prev.next = left
            if right:
                prev.next = right
            
            return dummy.next 
        
        if not head or not head.next:
            return head
        left = head 
        middle = findMid(head)
        temp = middle.next 
        middle.next = None 
        right = temp      
        
        left = self.sortList(left)
        right = self.sortList(right)
        
        return merge(left, right)
