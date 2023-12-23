class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        upper = len(nums)
        index = 0

        while index<upper:
            if nums[index]==val:
                del nums[index]
                upper -= 1
            else:
                index+=1

        return len(nums)