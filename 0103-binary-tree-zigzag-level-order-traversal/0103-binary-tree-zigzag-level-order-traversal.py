# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque()
        res = []
        q.append(root)
        change = True 
        while q :
            N = len(q)
            temp = []
            for i in range(len(q)): 
                curr = q.popleft()
                temp.append(curr.val)
                if curr.left :
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                    
            if change and temp :
                res.append(temp.copy())
            else:
                if temp :
                    res.append(temp[::-1])
            change = not change
        
        return res
            
        