class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        m = min(a,b)
        factors = 1
        
        for i in range(2,m+1):
            if a%i==0 and b%i==0:
                factors+=1

        return factors