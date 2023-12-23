class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        a = max(nums)

        return (k*(2*a + (k-1)))//2