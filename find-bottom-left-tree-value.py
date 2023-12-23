# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = [root]

        while queue:
            n = len(queue)
            first = queue.pop(0)
            if first.left is not None:
                queue.append(first.left)
            if first.right is not None:
                queue.append(first.right)
            for _ in range(n-1):
                node = queue.pop(0)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
        
        return first.val
