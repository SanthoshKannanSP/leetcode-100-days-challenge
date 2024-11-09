class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        left, right = k, k
        min_value = nums[k]
        max_score = min_value

        while left>0 or right<len(nums)-1:
            if (nums[left-1] if left>0 else 0) < (nums[right+1] if right<len(nums)-1 else 0):
                right += 1
                min_value = min(min_value,nums[right])
            else:
                left -= 1
                min_value = min(min_value,nums[left])

            max_score = max(max_score, min_value*(right-left+1))

        return max_score