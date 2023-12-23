# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        stack = []
        n = len(traversal)
        i = 0

        while i<n:
            level = 0
            val = ""
            while i<n and traversal[i]=="-":
                level+=1
                i+=1
            while i<n and traversal[i]!="-":
                val += traversal[i]
                i+=1
            while len(stack)>level:
                stack.pop()
            node = TreeNode(val)
            if stack and stack[-1].left is None:
                stack[-1].left = node
            elif stack:
                stack[-1].right = node
            stack.append(node)

        return stack[0]