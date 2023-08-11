class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        ans = []
        
        for candy in candies:
            if max_candies-candy>extraCandies:
                ans.append(False)
            else:
                ans.append(True)

        return ans