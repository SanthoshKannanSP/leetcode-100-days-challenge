class Solution:
    def numTrees(self, n: int) -> int:
        from math import factorial

        return int(factorial(2*n)/(factorial(n+1)*factorial(n)))