class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c = Counter(nums)
        
        v,m = 0,0
        ans = 0
        
        for i,j in c.items():
            if j>m:
                v=i
                m=j
                ans = j
            elif j==m:
                ans+=j
        return ans