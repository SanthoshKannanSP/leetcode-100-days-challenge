class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        queue = [root]
        while queue:
            n = len(queue)
            level_sum = 0
            for i in range(n):
                node = queue.pop(0)
                level_sum += node.val
                if not node.left is None:
                    queue.append(node.left)
                if not node.right is None:
                    queue.append(node.right)
        
        return level_sum