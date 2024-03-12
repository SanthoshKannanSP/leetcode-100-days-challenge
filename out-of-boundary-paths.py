class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        def dfs(i, j, remain):
            adj = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            if remain < 0:
                return 0

            if i < 0 or i >= m or j < 0 or j >= n:
                return 1

            if (i, j, remain) in dp:
                return dp[(i, j, remain)]

            res = 0 
            for di, dj in adj:
                di, dj = i + di, j + dj
                res += dfs(di, dj, remain - 1)

            dp[(i, j, remain)] = res % MOD

            return dp[(i, j, remain)]

        MOD = 10**9 + 7
        dp = dict()

        return dfs(startRow, startColumn, maxMove)