class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num==0:
            return True
        
        n = str(num)
        if n==n.strip("0"):
            return True
        return False