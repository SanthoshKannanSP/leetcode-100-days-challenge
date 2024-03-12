class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        m = 0
        nums.sort()

        while left<right:
            m = max(m,nums[left]+nums[right])
            left+=1
            right-=1
        
        return m