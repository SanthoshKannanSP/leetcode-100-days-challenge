class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        s = 0
        for i in range(1,n+1):
            if i%m==0:
                s-=i
            else:
                s+=i

        return s