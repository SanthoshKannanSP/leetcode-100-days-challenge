class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def condition(s):
            count = 1
            current_sum = 0
            for i in nums:
                current_sum += i

                if current_sum > s:
                    count+=1
                    current_sum = i

                if count > k:
                    return False
            
            return True

        left,right = max(nums),sum(nums)

        while left<right:
            mid = left + (right-left)//2
            if condition(mid):
                right = mid
            else:
                left = mid+1

        return left