class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        amount = 1
        ans = 0
        index = 0
        length = len(nums)

        while amount<=n:
            if index<length and nums[index]<=amount:
                amount += nums[index]
                index+=1
            else:
                amount += amount
                ans += 1

        return ans