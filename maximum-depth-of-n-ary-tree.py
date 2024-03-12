class Solution:
    def maxDepth(self, root: "Node") -> int:
        if root is None:
            return 0
        queue = deque([root])
        level = 0

        while queue:
            n = len(queue)
            level += 1
            for i in range(n):
                node = queue.popleft()
                for child in node.children:
                    queue.append(child)

        return level
