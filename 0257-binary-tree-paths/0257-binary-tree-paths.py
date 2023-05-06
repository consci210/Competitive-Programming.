from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        path = []

        def dfs(root, curr): 
            if not root or (not root.left and not root.right):
                path.append("->".join(curr))
                return 
            if root.left:
                curr.append (str((root.left.val)))
                dfs(root.left, curr)
                curr.pop()
            if root.right:
                curr.append (str((root.right.val)))
                dfs(root.right, curr)
                curr.pop()
        dfs(root, [str(root.val)])

        return path
