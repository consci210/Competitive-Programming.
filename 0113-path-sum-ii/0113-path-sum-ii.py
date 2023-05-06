# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        answer = []
        
        if not root :
            return 
        
        def dfs(root , path , total ) :
            if ( (not root.left and not root.right)) and total == targetSum  :
                answer.append(path.copy())
                return 
            
            if root.left :
                path.append(root.left.val)
                total+=root.left.val
                dfs(root.left , path , total)
                path.pop()
                total-=root.left.val
                
            if root.right :
                path.append(root.right.val)
                total+=root.right.val
                dfs(root.right , path , total)
                path.pop()
                total-=root.right.val
                
        dfs(root , [root.val] , root.val)
        return answer 