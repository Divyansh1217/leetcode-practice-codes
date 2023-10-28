# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def fd(node,s):
            if not node:
                return 
            s=s+ (node.val)
            if node.left == None and node.right == None:
                if s== targetSum:
                    return True
            return fd(node.left,s) or fd(node.right,s)
        return fd(root,0)