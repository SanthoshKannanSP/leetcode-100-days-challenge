class Solution:
    def trap(self, height: List[int]) -> int:
        i,j = 0,len(height)-1
        left_max = height[i]
        right_max = height[j]
        ans = 0

        while i<j:
            if left_max<=right_max:
                ans += left_max-height[i]
                i += 1
                left_max = max(left_max,height[i])
            else:
                ans += right_max-height[j]
                j -= 1
                right_max = max(right_max,height[j])

        return ans