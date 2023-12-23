class Solution:
    def maxScore(self, s: str) -> int:
        o,z = 0,0
        m = -1
        n = len(s)

        for i in range(n-1):
            if s[i]=="1":
                o+=1
            else:
                z+=1
            m = max(m,z-o)
        
        if s[-1]=="1":
            o+=1

        return m+o