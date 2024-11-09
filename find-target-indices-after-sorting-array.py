class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        less = 0
        equal = 0

        for i in nums:
            if i<target:
                less+=1
            elif i==target:
                equal+=1

        return [i for i in range(less,less+equal)]