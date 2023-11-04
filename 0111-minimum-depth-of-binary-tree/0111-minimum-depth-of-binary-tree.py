# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        lh,rh=self.minDepth(root.left),self.minDepth(root.right)
        if root.left ==None and root.right == None:
            return 1
        if root.left ==None:
            return 1+rh
        if root.right==None:
            return 1+lh
        return min(lh,rh) +1
        