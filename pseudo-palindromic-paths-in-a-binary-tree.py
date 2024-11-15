class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        count = 0
        stack = [(root, 0)]

        while stack:
            node, path = stack.pop()
            if node:
                path ^= 1 << node.val
                if node.left is None and node.right is None:
                    if path & (path - 1) == 0:
                        count += 1
                else:
                    stack.append((node.left, path))
                    stack.append((node.right, path))

        return count