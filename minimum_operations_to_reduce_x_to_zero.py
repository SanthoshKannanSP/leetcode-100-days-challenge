class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        s = sum(nums)
        max_length = -1
        window_sum = 0

        left = 0

        for right in range(len(nums)):
            window_sum += nums[right]
            
            while left<=right and window_sum > s-x:
                window_sum -= nums[left]
                left+=1

            if window_sum==s-x:
                print(left,right,window_sum)
                max_length = max(max_length,right-left+1)

        if max_length==-1:
            return -1
        else:
            return len(nums)-max_length