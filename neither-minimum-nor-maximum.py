class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        n = len(nums)
        if len(nums)<=2:
            return -1
        mi = nums[0]
        ma = nums[0]
        for i in range(1,n):
            mi = min(mi,nums[i])
            ma = max(ma,nums[i])

        for i in range(n):
            if mi<nums[i]<ma:
                return nums[i]