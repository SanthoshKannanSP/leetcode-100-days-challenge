# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = 0
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(node,stack):
            stack.append(str(node.val))
            if node.left is None and node.right is None:
                self.ans += int("".join(stack))
            else:
                if node.left:
                    dfs(node.left,stack)
                if node.right:
                    dfs(node.right,stack)
            stack.pop()
            return
            
        dfs(root,[])
        return self.ans