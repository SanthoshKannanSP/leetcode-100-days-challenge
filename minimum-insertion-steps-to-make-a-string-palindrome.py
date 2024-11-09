class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        rev = s[::-1]
        dp = [[0]*(n+1) for _ in range(n+1)]

        for i,c in enumerate(s):
            for j,v in enumerate(rev):
                dp[i+1][j+1] = dp[i][j]+1 if c==v else max(dp[i][j+1],dp[i+1][j])
        
        return n - dp[n][n]