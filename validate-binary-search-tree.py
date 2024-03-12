class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(root,start,end):
            if not root:
                return True

            if root.val > end or root.val < start:
                return False 

            if root.left and root.left.val>=root.val:
                return False
            if root.right and root.right.val<=root.val:
                return False

            return isValid(root.left,start,root.val-1) and isValid(root.right,root.val+1,end)

        return isValid(root,-float("inf"),float("inf"))