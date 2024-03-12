class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1

        while l<r:
            s = numbers[l] + numbers[r]
            if s==target:
                break
            if s<target:
                l+=1
            else:
                r-=1

        return [l+1,r+1]