class Solution:
    def countPoints(self, rings: str) -> int:
        d = defaultdict(set)
        n = len(rings)
        ans = 0

        for i in range(0,n,2):
            d[rings[i+1]].add(rings[i])

        for i in d:
            if len(d[i])==3:
                ans+=1
        return ans