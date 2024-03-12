class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        c = Counter(nums)

        return sum([i for i in c if c[i]==1])