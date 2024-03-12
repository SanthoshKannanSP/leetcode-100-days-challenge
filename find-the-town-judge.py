class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        deg = [0]*n

        for s,d in trust:
            deg[d-1]+=1
            deg[s-1]-=1

        for i,v in enumerate(deg):
            if v==n-1:
                return i+1

        return -1