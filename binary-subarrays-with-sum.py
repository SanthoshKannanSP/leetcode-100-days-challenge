class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        ans = 0
        csum = 0
        dp = defaultdict(int)
        dp[0] = 1

        for num in nums:
            csum += num
            ans += dp[csum-goal]
            dp[csum] += 1

        return ans