class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = float("-inf")

        def dfs(node):
            nonlocal max_path
            if node is None:
                return 0

            left = max(dfs(node.left),0)
            right = max(dfs(node.right),0)

            path = node.val + left + right
            max_path = max(max_path, path)

            return node.val + max(left,right)

        dfs(root)
        return max_path