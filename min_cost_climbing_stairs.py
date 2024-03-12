class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = dict()
        dp[0],dp[1] = cost[0],cost[1]

        def cost_to_n_stair(n):
            if n<0:
                return 0
            if n in dp:
                return dp[n]
            
            dp[n] = cost[n] + min(cost_to_n_stair(n-1),cost_to_n_stair(n-2))
            return dp[n]

        return min(cost_to_n_stair(n-1),cost_to_n_stair(n-2))