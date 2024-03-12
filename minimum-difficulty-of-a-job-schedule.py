class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        from functools import lru_cache

        n = len(jobDifficulty)
        if n<d:
            return -1

        @lru_cache(None)
        def dfs(i,k):
            if k==d:
                return max(jobDifficulty[i:])
            res, maxd = float("inf"), 0
            for j in range(i,n-d+k):
                maxd = max(maxd,jobDifficulty[j])
                res = min(res,maxd+dfs(j+1,k+1))
            return res

        return dfs(0,1)