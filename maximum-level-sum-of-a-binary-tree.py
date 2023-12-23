# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        s = -float("inf")
        l = 0
        ml = 0
        queue = [root]

        while queue:
            n = len(queue)
            l += 1
            curr = 0
            for _ in range(n):
                node = queue.pop(0)
                curr += node.val
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            if curr>s:
                s = curr
                ml = l
        
        return ml