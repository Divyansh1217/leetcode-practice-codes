# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        res=0
        q=[(root,0)]
        
        while q:
            node,l=q.pop(0)
            if (not node.left) and (not node.right) and l:
                res+=node.val
            if node.left:
                q.append((node.left,1))
            if node.right:
                q.append((node.right,0))
        
        return res