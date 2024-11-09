class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        s = set()
        ans = 0

        for roll in rolls:
            s.add(roll)
            if len(s)==k:
                ans+=1
                s.clear()
        
        return ans+1