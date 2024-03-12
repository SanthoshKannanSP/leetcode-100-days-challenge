class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0]*(n+1)

        for start in range(n-1,-1,-1):
            c_max = 0
            end = min(n, start + k)

            for i in range(start, end):
                c_max = max(c_max, arr[i])
                dp[start] = max(dp[start], dp[i+1]+c_max*(i-start+1))

        return dp[0]