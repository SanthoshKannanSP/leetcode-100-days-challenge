class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        R,C = len(matrix), len(matrix[0])
        dp = [[-1]*C for _ in range(R)]

        def dfs(r,c,prev):
            if r<0 or r>R-1 or c<0 or c>C-1 or matrix[r][c]<=prev:
                return 0

            if dp[r][c]==-1:
                down = dfs(r+1,c,matrix[r][c])
                up = dfs(r-1,c,matrix[r][c])
                right = dfs(r,c+1,matrix[r][c])
                left = dfs(r,c-1,matrix[r][c])

                dp[r][c] = 1 + max(up,down,left,right)

            return dp[r][c]

        ans = 0
        for row in range(R):
            for col in range(C):
                ans = max(ans,dfs(row,col,-1))
        
        return ans