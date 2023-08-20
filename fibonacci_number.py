class Solution:
    dp = {
        0:0,
        1:1
    }
    def fib(self, n: int) -> int:
        if n in self.dp:
            return self.dp[n]
        
        self.dp[n] = self.fib(n-1)+self.fib(n-2)
        return self.dp[n]