class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [nums[0]]
        for i in range(1,n):
            prefix.append(prefix[-1]+nums[i])

        ans = []

        for i in range(n):
            left = prefix[i]-nums[i]
            right = prefix[-1]-prefix[i]

            left_tot = i*nums[i] - left
            right_tot = right - (n-i-1)*nums[i]

            ans.append(left_tot+right_tot)

        return ans