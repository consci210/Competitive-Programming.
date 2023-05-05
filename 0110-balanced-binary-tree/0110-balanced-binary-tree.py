# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool: 
        
        def check(root):
            if not root :
                return [True , 0]
            
            left = check(root.left)
            right = check(root.right)
            
            is_balanced = (( abs(left[1] - right[1])) <= 1  and left[0] and right[0])
            
            return ([is_balanced , 1 + max( left[1] , right[1]) ] )
        
        return check(root)[0]    
        