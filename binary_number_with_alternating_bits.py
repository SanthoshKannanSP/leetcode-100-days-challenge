class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        tmp = (n>>1)+n
        return (tmp & tmp+1)==0