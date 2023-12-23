class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        n = len(nums)
        s = 0
        for i in range(n):
          if i.bit_count()==k:
            s+=nums[i]
        
        return s