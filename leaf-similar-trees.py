class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node,l):
            if node is None:
                return l
            if node.left is None and node.right is None:
                l.append(node.val)
            left = dfs(node.left,l)
            right = dfs(node.right,l)
            return l

        leaf1 = dfs(root1,[])
        leaf2 = dfs(root2,[])
        if len(leaf1)!=len(leaf2):
            return False
        
        for i in range(len(leaf1)):
            if leaf1[i]!=leaf2[i]:
                return False
        
        return True