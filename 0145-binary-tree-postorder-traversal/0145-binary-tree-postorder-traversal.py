# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root==None:
            return
        a=[]
        s=[root]
        while s:
            node=s.pop()
            a.append(node.val)
            if node.left:
                s.append(node.left)
            if node.right:
                s.append(node.right)
        return a[::-1]