class Solution:
    dp = {
        0:0,
        1:1,
        2:1
    }
    def tribonacci(self, n: int) -> int:
        if n in self.dp:
            return self.dp[n]
        
        self.dp[n] = self.tribonacci(n-1)+self.tribonacci(n-2)+self.tribonacci(n-3)
        return self.dp[n]