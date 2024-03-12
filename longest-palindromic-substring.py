class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[0]*n for i in range(n)]
        start,end = 0,0

        for i in range(n):
            dp[i][i] = 1

        for i in range(n-1):
            if s[i]==s[i+1]:
                dp[i][i+1] = 1
                start,end = i,i+1

        for length in range(2,n):
            for i in range(n-length):
                j = i+length
                if s[i]==s[j] and dp[i+1][j-1]==1:
                    dp[i][j] = 1
                    start,end = i,j

        return s[start:end+1]