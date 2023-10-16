# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        a=[]
        def ans(root,s):
            s=s+str(root.val)
            if not root.right and not root.left:
                a.append(s)
                return
            if root.right:
                ans(root.right,s+"->")
            if root.left:
                ans(root.left,s+"->")
        ans(root,"")
        return a