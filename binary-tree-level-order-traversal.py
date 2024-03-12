class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([root])
        ans = []

        while q:
            d = []
            n = len(q)
            for i in range(n):
                node = q.popleft()
                if not node:
                    continue
                d.append(node.val)
                q.append(node.left)
                q.append(node.right)
            if not d:
                continue
            ans.append(d)
        
        return ans