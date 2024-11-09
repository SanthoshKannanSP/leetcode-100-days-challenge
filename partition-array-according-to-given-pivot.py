class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        ans = []
        count = 0

        for i in range(n):
            if nums[i]<pivot:
                ans.append(nums[i])
            elif nums[i]==pivot:
                count+=1

        for i in range(count):
            ans.append(pivot)

        for i in range(n):
            if nums[i]>pivot:
                ans.append(nums[i])

        return ans