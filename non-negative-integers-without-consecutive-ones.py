class Solution:
    def findIntegers(self, n: int) -> int:
        dp = [1,2]

        for i in range(2,30):
            dp.append(dp[-1]+dp[-2])
        
        ans, last_seen = 0, 0
        for i in reversed(range(30)):
            if (1<<i)&n:
                ans+=dp[i]
                if last_seen:
                    ans-=1
                    break
                last_seen = 1
            else:
                last_seen = 0
        
        return ans+1