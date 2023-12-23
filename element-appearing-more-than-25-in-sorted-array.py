class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)

        count = 1

        for index in range(1,n):
            if arr[index]!=arr[index-1]:
                count = 0

            count += 1
            if count>n//4:
                return arr[index] 
        
        return arr[0]