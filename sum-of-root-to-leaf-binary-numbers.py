class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        stack = deque([[root,0]])
        ans = 0

        while stack:
            node,val = stack.popleft()
            val = (val<<1) + node.val
            if node.left:
                stack.append([node.left,val])
            if node.right:
                stack.append([node.right,val])

            if not node.left and not node.right:
                ans += val

        return ans