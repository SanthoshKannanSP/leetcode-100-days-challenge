class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_length = 0

        for i in nums:
            if i-1 not in nums:
                l = i+1
                while l in nums:
                    l+=1
                max_length = max(max_length,l-i)

        return max_length