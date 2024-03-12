class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n = len(s)
        dp = [[float("inf")]*101 for _ in range(101)]

        dp[0][0] = 0

        for i in range(1,n+1):
            for j in range(k+1):
                count, del_count = 0,0

                for t in range(i,0,-1):
                    if s[t-1]==s[i-1]:
                        count+=1
                    else:
                        del_count += 1
                    
                    if j-del_count >= 0:
                        temp = 0

                        if count>=100:
                            temp=3
                        elif count>=10:
                            temp=2
                        elif count>=2:
                            temp=1

                        dp[i][j] = min(dp[i][j],dp[t-1][j-del_count]+1+temp)
                if j>0:
                    dp[i][j] = min(dp[i][j],dp[i-1][j-1])

        return dp[n][k]