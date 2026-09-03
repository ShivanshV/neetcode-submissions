# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def helper(root, smallest, largest):
            if root is None:
                return True
            
            if root.val >= largest or root.val <= smallest:
                return False
            
            return helper(root.left, smallest, root.val) and helper(root.right, root.val, largest)
          
        return helper(root, float('-inf'), float('inf'))