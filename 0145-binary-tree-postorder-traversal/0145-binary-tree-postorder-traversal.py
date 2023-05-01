# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # left right root
        res = []
        def dfs(root=root):
            if not root :
                return 
            dfs(root.left)
            dfs(root.right)
            res.append(root.val)
        dfs()
        return res