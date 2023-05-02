# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right :
            return True 
        if not root.left or not root.right:
            return False 
        r1 = root.left
        r2 = root.right 
        
        def check( root1 , root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False 
            if root1.val != root2.val :
                return False     
            return check(root1.left , root2.right) and check(root2.left , root1.right)
        return check(r1,r2)