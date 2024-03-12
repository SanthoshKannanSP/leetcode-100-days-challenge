class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = [0]*len(nums)
        l = 0
        for i in nums:
            start,end = 0,l
            while start!=end:
                mid = (start+end)//2
                if tails[mid]<i:
                    start = mid+1
                else:
                    end = mid
            tails[start] = i
            l = max(start+1,l)
        return l