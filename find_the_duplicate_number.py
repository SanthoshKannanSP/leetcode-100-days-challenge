class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = dict()

        for i in nums:
            if i in d:
                return i
            else:
                d[i] = 1