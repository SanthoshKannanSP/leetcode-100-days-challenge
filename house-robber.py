class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = dict()
        n = len(nums)

        if n<3:
            return max(nums)

        def dfs(index):
            if index>=n:
                return 0
            
            if index not in dp:
                chose1 = nums[index]+dfs(index+2)
                chose2 = nums[index]+dfs(index+3)

                dp[index] = max(chose1,chose2)

            return dp[index]

        ans = max(dfs(0),dfs(1))
        return ans