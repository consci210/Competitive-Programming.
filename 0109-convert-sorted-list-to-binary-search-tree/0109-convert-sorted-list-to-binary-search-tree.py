# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        
        count = 0 
        curr = head 
        while curr :
            curr = curr.next
            count += 1
            
        self.head = head 
        
        def convert(start , end ): 
            if (start>end): return None 
            mid = (start +end)//2
            left = convert(start , mid-1)
            root = TreeNode(self.head.val)
            self.head = self.head.next
            root.left = left 
            root.right = convert(mid+1 , end )
            
            return root 
        return(convert(0 , count-1))