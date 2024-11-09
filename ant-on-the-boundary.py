class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        p = 0
        ans = 0

        for i in nums:
            p+=i
            if p==0:
                ans+=1

        return ans