class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m,n = len(matrix),len(matrix[0])
        
        sub_sum = [[0]*n for _ in range(m)]

        for r in range(m):
            for c in range(n):
                top = sub_sum[r-1][c] if r>0 else 0
                left = sub_sum[r][c-1] if c>0 else 0
                topleft = sub_sum[r-1][c-1] if min(r,c)>0 else 0

                sub_sum[r][c] = matrix[r][c] + top + left - topleft

        ans = 0
        for r1 in range(m):
            for r2 in range(r1,m):
                dp = defaultdict(int)
                dp[0] = 1
                for c in range(n):
                    cs = sub_sum[r2][c] - (
                        sub_sum[r1-1][c] if r1>0 else 0
                    )
                    rem = cs-target

                    ans += dp[rem]
                    dp[cs] += 1

        return ans