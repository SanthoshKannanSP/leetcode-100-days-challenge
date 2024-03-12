class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        freq = Counter(nums)
        ans = []

        for i in range(1,max(freq.values())+1):
            ans.append([j for j in freq if freq[j]>=i])
        
        return ans