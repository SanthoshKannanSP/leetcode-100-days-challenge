class Solution:
    def numDecodings(self, s: str) -> int:
        dp = defaultdict(int)

        def dfs(index):
            if index == len(s):
                return 1
            if s[index] == "0":
                return 0
            if index in dp:
                return dp[index]

            ways = dfs(index + 1)
            if index + 1 < len(s) and int(s[index : index + 2]) <= 26:
                ways += dfs(index + 2)

            dp[index] = ways

            return ways

        return dfs(0)
