# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root , largest , smallest ):
            if not root :
                return True 
            
            if root.val >= largest or root.val <= smallest :
                return False 
        
            return (dfs(root.left , root.val , smallest ) and dfs(root.right , largest , root.val))  

        return dfs(root , inf , -inf )