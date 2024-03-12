class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        indegree = defaultdict(int)
        outdegree = defaultdict(int)
        for w,l in matches:
            indegree[l] += 1
            outdegree[w] += 1

        ans = [[],[]]

        for p in indegree:
            if indegree[p]==1:
                ans[1].append(p)

        for p in outdegree:
            if indegree[p]==0:
                ans[0].append(p)

        return [sorted(i) for i in ans]