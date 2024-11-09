class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        nums=[]
        for row in values:
            for val in row:
                nums.append(val)

        ans=0
        c=1
        nums.sort()

        for n in nums:
            ans += c*n
            c += 1

        return ans