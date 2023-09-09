class Solution:
    ans = []
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.ans = []
        def dfs(stack,node,target):
            if node is None:
                return
            stack.append(node.val)
            target-=node.val
            
            if target==0 and node.left is None and node.right is None:
                self.ans.append(stack[:])
                stack.pop()
                return

            if node.left is None and node.right is None:
                stack.pop()
                return

            if not node.left is None:
                dfs(stack,node.left,target)
            
            if not node.right is None:
                dfs(stack,node.right,target)
            
            target+=node.val
            stack.pop()

            return

        dfs([],root,targetSum)
        return self.ans