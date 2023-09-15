class Solution:
    ans = []
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.ans = []
        n = len(graph)-1

        def dfs(stack,node):
            if node is None:
                return
            stack.append(node)
            print(stack)
            if node == n:
                
                self.ans.append(stack[:])
                return
            
            for i in graph[node]:
                dfs(stack[:],i)
            
            return

        dfs([],0)

        return self.ans