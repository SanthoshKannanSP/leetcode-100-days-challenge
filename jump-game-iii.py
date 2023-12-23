class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if start<0 or start>=len(arr) or arr[start]<0:
            return False
        
        if arr[start]==0:
            return True
        else:
            arr[start]*=-1
            return self.canReach(arr,start+arr[start]) or self.canReach(arr,start-arr[start])