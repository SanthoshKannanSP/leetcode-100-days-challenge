class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        s = 0
        for i in nums:
            s+=i
            for j in str(i):
                s-=int(j)

        return s