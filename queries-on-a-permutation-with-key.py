class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        q = deque([i for i in range(1,m+1)])
        ans = []
        
        for i in queries:
            s = q.index(i)
            ans.append(s)
            q.remove(i)
            q.appendleft(i)

        return ans