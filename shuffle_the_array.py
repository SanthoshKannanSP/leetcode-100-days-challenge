class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        for index in range(n):
            ans.append(nums[index])
            ans.append(nums[index+n])

        return ans