class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        n = len(costs)
        costs.sort()
        index = 0

        while index<n and coins>=costs[index]:
            coins -= costs[index]
            index+=1
        
        return index