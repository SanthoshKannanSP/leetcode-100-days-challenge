class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)-1

        for i in range(n,0,-1):
            for j in range(i):
                nums[j] += nums[j+1]
                nums[j]%=10

        return nums[0]