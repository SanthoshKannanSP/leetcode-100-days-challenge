class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        def dfs(node):
            if node is None:
                return
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
            dfs(node.left)
            dfs(node.right)

        graph = defaultdict(list)
        dfs(root)
        visited = set()
        queue = deque([start])
        level = -1

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                visited.add(node)
                for neighbour in graph[node]:
                    if neighbour not in visited:
                        queue.append(neighbour)
            level += 1

        return level