# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root :
            return 0 
        self.count = 0
        def check(node , greatest):
            if not node :
                return  
            if node.val >= greatest:
                self.count += 1
                greatest = node.val 
            check(node.left , greatest)
            check(node.right , greatest)
        
        check(root,root.val)
        return self.count
                