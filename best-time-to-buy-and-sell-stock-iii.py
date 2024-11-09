class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        b1,b2 = float("inf"),float("inf")
        s1,s2 = 0,0
        for price in prices:
            b1 = min(b1,price)
            s1 = max(s1,price-b1)
            b2 = min(b2,price-s1)
            s2 = max(s2,price-b2)

        return s2