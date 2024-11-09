class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)

        if n<2:
            return ans

        end = 0
        ma = 0
        index = 0

        while True:
            while index<=end:
                ma = max(ma,nums[index]+index)
                if ma>=n-1:
                    return ans+1
                index+=1
            
            if end < ma:
                end = ma
                ans+=1