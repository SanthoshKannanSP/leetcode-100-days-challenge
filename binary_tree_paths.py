class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if root.left is None and root.right is None:
            return [str(root.val)]
        
        ans = []
        if root.left is not None:
            left_list = self.binaryTreePaths(root.left)
            for i in left_list:
                ans.append(str(root.val)+"->"+i)

        if root.right is not None:
            right_list = self.binaryTreePaths(root.right)
            for i in right_list:
                ans.append(str(root.val)+"->"+i)

        return ans