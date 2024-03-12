class Solution:
    s = 0
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def postOrder(root,s=0):
            if not root:
                return
            postOrder(root.right)
            root.val, self.s = self.s+root.val, root.val+self.s
            postOrder(root.left)
            return

        self.s = 0
        postOrder(root)
        return root