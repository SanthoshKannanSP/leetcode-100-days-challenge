class Solution:
    def numberOfWays(self, corridor: str) -> int:
        seats = 0
        prev = 0
        ans = 1

        for curr in range(len(corridor)):
            if corridor[curr]=="S":
                if seats<2:
                    seats+=1
                else:
                    seats=1
                    ans *= (curr-prev)
                prev = curr

        return 0 if seats<2 else ans%(10**9+7)