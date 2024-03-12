class Solution:
    diff = 0
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.diff = 0
        def dfs(root,mi,ma):
            if not root:
                return
            self.diff = max(self.diff,max(abs(mi-root.val),abs(ma-root.val)))
            mi = min(mi,root.val)
            ma = max(ma,root.val)
            dfs(root.left,mi,ma)
            dfs(root.right,mi,ma)

            return

        if not root:
            return 0
        dfs(root,root.val,root.val)
        return self.diff