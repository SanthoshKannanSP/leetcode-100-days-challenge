# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    count = 0
    def dfs(self,node):
        if node is None:
            return 0,0
        left,lcount = self.dfs(node.left)
        right,rcount = self.dfs(node.right)

        s = left+right+node.val
        ncount = lcount+rcount+1
        if node.val==s//ncount:
            self.count += 1

        return s,ncount

    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        self.dfs(root)
        return self.count