# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        a={}
        def hell(node):
            if not node:
                return False
            if node.val in a:
                return True
            a[k - node.val] =True
            return hell(node.left) or hell(node.right)
        return hell(root)