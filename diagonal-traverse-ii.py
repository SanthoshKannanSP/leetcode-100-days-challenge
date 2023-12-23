class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        d = defaultdict(list)
        ans = []
        
        for i in range(n):
            for j in range(len(nums[i])):
                d[i+j].append(nums[i][j])

        for i in range(max(d)+1):
            for j in d[i][::-1]:
                ans.append(j)

        return ans