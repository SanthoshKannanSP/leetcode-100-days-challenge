class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = [root]
        ans = []

        while queue:
            n = len(queue)
            s = 0
            for i in range(n):
                node = queue.pop(0)
                s += node.val
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            ans.append(s / n)

        return ans
