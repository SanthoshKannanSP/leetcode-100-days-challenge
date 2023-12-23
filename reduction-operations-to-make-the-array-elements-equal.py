class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        accum = 0

        for i in range(1,n):
            if nums[i]!=nums[i-1]:
                accum += 1
            
            ans += accum

        return ans