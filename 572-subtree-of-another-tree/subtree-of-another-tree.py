# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #Order is important
        if not subRoot: return True 
        #Checks if subroot is empty
        if not root: return False 
        #Checks if root is empty, since above condition is passed so subroot is non-empty hence return False

        if self.isSame(root, subRoot):
            return True
        return(self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

    def isSame(self, root, subRoot):
        if not root and not subRoot:
            return True
        if root and subRoot and root.val == subRoot.val:
            return (self.isSame(root.left, subRoot.left) and 
                    self.isSame(root.right, subRoot.right))
        return False
    
