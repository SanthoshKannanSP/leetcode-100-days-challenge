# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if node is None:
                return []
            return dfs(node.left) + [node.val] + dfs(node.right)

        ordered = dfs(root)

        def balance(l,r):
            if l>r:
                return None
            m = (l+r)//2
            root = TreeNode(ordered[m])
            root.left = balance(l,m-1)
            root.right = balance(m+1,r)
            return root

        return balance(0,len(ordered)-1)