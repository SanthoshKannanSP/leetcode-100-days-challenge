class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0]*n
        pos,neg = 0,1

        for i in nums:
            if i>0:
                ans[pos] = i
                pos+=2
            else:
                ans[neg] = i
                neg+=2

        return ans