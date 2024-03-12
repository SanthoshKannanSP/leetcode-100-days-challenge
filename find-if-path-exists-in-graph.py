class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        neighbours = defaultdict(list)

        for u,v in edges:
            neighbours[u].append(v)
            neighbours[v].append(u)

        stack = [source]
        visited = set()

        while stack:
            node = stack.pop()
            if node in visited:
                continue
            if node == destination:
                return True
            visited.add(node)

            for neighbour in neighbours[node]:
                stack.append(neighbour)

        return False