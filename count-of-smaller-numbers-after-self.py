class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        N = len(nums)-1
        ans = []

        for i in nums:
            index = bisect_left(sorted_nums,i)
            ans.append(index)
            sorted_nums.pop(index)
            N-=1

        return ans