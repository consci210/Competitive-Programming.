class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
                
        def check(root):
            if not root:
                return False 
            if root.val == subRoot.val and identical(root, subRoot):
                return True 
            return check(root.left) or check(root.right)
        
        def identical(root1, root2):
            if not root1 and not root2:
                return True 
            if not root1 or not root2:
                return False 
            return (root1.val == root2.val and 
                    identical(root1.left, root2.left) and 
                    identical(root1.right, root2.right))
        
        return check(root)
