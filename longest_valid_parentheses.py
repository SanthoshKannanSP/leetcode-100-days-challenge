class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        dp = defaultdict(int)
        max_count = 0
        for i in range(1,n):
            if s[i] == ")":
                if s[i-1] == "(":
                    dp[i] = dp[i-2] + 2
                elif i - dp[i-1] > 0 and s[i - dp[i-1] - 1] == "(":
                    dp[i] = dp[i-1] + dp[i-dp[i-1]-2] + 2
            max_count = max(max_count,dp[i])
        return max_count