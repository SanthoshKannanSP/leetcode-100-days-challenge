class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sorted_nums = sorted(nums)
        
        count = 0
        pos = dict()

        for i in sorted_nums:
            if i not in pos:
                pos[i] = count
            count+=1

        return [pos[i] for i in nums]