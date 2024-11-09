class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        stack1 = []
        stack2 = []

        while original or stack1:
            while original:
                stack1.append(original)
                stack2.append(cloned)
                original = original.left
                cloned = cloned.left

            original = stack1.pop()
            cloned = stack2.pop()

            if original==target:
                return cloned

            original = original.right
            cloned = cloned.right

        return cloned