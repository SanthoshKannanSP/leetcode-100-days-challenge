# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ""
        
        left = self.tree2str(root.left)
        right = self.tree2str(root.right)

        if right!="":
            right = "("+right+")"
            if left!="":
                left = "("+left+")"
            else:
                left = "()"
        else:
            if left!="":
                left = "("+left+")"

        return str(root.val)+left+right