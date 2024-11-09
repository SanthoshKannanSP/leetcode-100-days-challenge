class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cs = 0
        ans = 0
        dp = defaultdict(int)
        dp[0] = 1

        for i in nums:
            cs+=i
            rem = cs-k

            if rem in dp:
                ans += dp[rem]
            
            dp[cs] += 1

        return ans