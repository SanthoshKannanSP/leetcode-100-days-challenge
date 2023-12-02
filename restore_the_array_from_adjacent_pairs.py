class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for x,y in adjacentPairs:
            graph[x].append(y)
            graph[y].append(x)

        start = 0
        for node in graph:
            if len(graph[node])==1:
                start = node
                break

        def dfs(node,prev,ans):
            ans.append(node)
            for neighbour in graph[node]:
                if neighbour!=prev:
                    dfs(neighbour,node,ans)

        ans = []
        dfs(start,None,ans)
        return ans