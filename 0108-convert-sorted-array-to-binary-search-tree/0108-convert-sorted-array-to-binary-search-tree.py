# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:   
        
        def convert(l , r ):
            
            if l > r :
                return
            
            m = (l+r)//2
            root = TreeNode(nums[m])
            root.left = convert(l,m-1) 
            root.right = convert(m+1 , r)
            return root 
        return convert(0 , len(nums)-1 )