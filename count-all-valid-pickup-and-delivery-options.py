class Solution:
    def countOrders(self, n: int) -> int:
        MOD = 10**9 + 7
        ans = 1
        for i in range(1, n+1):
            num_pickups = 2*(i-1)+1
            ans = ans * (num_pickups+1) * num_pickups // 2
        return ans % MOD