class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freq = Counter(nums)
        ans = 0
        for i in freq.values():
            if i==1:
                return -1
            ans += ceil(i/3)
        
        return ans