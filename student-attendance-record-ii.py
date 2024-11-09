class Solution:
    def checkRecord(self, n: int) -> int:
        dp = [[[-1 for _ in range(3)] for _  in range(2)] for _ in range(n)]
        MOD = 10**9 + 7

        def dfs(d,a,l):
            if d==n:
                return 1
            
            if dp[d][a][l] != -1:
                return dp[d][a][l]

            next_a = dfs(d+1,a+1,0) if a==0 else 0
            next_l = 0 if l==2 else dfs(d+1,a,l+1)
            next_p = dfs(d+1,a,0)

            ans = (next_a + next_l + next_p) % MOD

            dp[d][a][l] = ans
            return ans

        return dfs(0,0,0)