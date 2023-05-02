# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode] , count=0) -> int:
        
        def depth(root=root , count=0):
            if not root :
                return count 
        
            if root :
                count+=1
            
            return (max(depth(root.left , count) , depth (root.right , count)))
        
        return depth()