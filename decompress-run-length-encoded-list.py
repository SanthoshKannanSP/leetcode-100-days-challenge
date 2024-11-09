class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)

        for i in range(0,n,2):
            ans += [nums[i+1]]*nums[i]

        return ans