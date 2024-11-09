class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        incr = [(x^k)-x for x in nums]
        n = len(nums)
        ans = sum(nums)
        incr = sorted(incr, reverse=True)
        
        for i in range(1,n,2):
            if incr[i]+incr[i-1] > 0:
                ans += incr[i]+incr[i-1]

        return ans