class Solution:
    from functools import lru_cache
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)

        @lru_cache(None)
        def dp(i,j):
            if i>j:
                return 0
            player = (n-j+i)%2
            if player==1:
                return max(piles[i]+dp(i+1,j), piles[j]+dp(i,j-1))
            else:
                return min(-piles[i]+dp(i+1,j), -piles[j]+dp(i,j-1))

        return dp(0,n-1) > 0