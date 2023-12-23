class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        left = [0]
        right = [0]

        for i in range(n):
            left.append(left[-1]+nums[i])

        for i in range(n-1,-1,-1):
            right.append(right[-1]+nums[i])

        right = right[::-1]

        return [abs(left[i]-right[i+1]) for i in range(n)]