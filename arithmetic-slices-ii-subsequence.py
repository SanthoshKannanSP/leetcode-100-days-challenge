class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n)]

        ans = 0
        for i in range(1,n):
            for j in range(i):
                diff = nums[i] - nums[j]
                count = 0
                if diff in dp[j]:
                    count = dp[j][diff]
                
                dp[i][diff] += count+1
                ans += count
        
        return ans