class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        n = len(nums)
        m = len(numsDivide)

        def calculate_hcf(i,j):
            while j>0:
                i,j = j,i%j
            return i

        numsDivide.sort()
        hcf = numsDivide[0]

        for i in range(1,m):
            hcf = calculate_hcf(numsDivide[i],hcf)

        nums.sort()

        for i,val in enumerate(nums):
            if val>hcf:
                return -1
            elif hcf%val==0:
                return i

        return -1