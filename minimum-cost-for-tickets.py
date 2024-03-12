class Solution:
    dp = dict()
    def mincostTickets(self, days: List[int], costs: List[int],reset=True) -> int:
        if reset:
            self.dp = dict()
        c = float("inf")
        d = days[0]
        if d not in self.dp:
            if len(days)>1:
                c = min(c,costs[0]+self.mincostTickets(days[1:],costs,False))
            else:
                c = min(c,costs[0])
            
            i = 0
            while i<len(days) and days[i]<days[0]+7:
                i+=1
            
            if len(days)>i:
                c = min(c,costs[1]+self.mincostTickets(days[i:],costs,False))
            else:
                c = min(c,costs[1])
            
            while i<len(days) and days[i]<days[0]+30:
                i+=1
            
            if len(days)>i:
                c = min(c,costs[2]+self.mincostTickets(days[i:],costs,False))
            else:
                c = min(c,costs[2])

            self.dp[d]=c

        return self.dp[d]