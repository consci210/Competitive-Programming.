# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root :
            return ([])
        queue = deque()
        queue.append(root)
        ans = []
        ans.append([root.val])
        while queue :
            temp = []
            for i in range(len(queue)):
                curr = queue.popleft()    
                if curr.left :
                    queue.append(curr.left)
                    temp.append(curr.left.val) 
                if curr.right :
                    queue.append(curr.right)
                    temp.append(curr.right.val)
            if temp :
                ans.append(temp.copy()) 
            
        return ans
                