class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        s = 0
        left = 0
        n = len(nums)

        for right in range(n):
            s += nums[right]
            while s*(right-left+1) >= k:
                s -= nums[left]
                left += 1
            ans += right-left+1

        return ans