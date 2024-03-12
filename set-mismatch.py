class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dup = 0
        s = 0
        n = len(nums)
        ss = (n*(n+1))//2
        
        for i in nums:
            j = abs(i)
            if nums[j-1]<0:
                dup = j
            s+=j
            nums[j-1]*=-1

        return [dup,ss-s+dup]