# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not subRoot:
            return True
        if not root:
            return False

        def sameTree(h1,h2):
            if not h1 and not h2:
                return True
            if not h1 or not h2:
                return False
            if h1.val != h2.val:
                return False
            
            return (sameTree(h1.left,h2.left) and sameTree(h1.right,h2.right))

        if sameTree(root,subRoot):
            return True
        else:
            return (self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot))