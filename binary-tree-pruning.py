class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]: 
        if root is None :
            return None
        if self.pruneTree(root.left) is None  :
            root.left = None
        if self.pruneTree(root.right) is None : 
            root.right = None
        if root.val!=1 and root.left is None and root.right is None:
            root=None
            
        return root